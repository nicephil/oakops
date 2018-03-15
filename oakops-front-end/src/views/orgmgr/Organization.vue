<template>
	<section>
		<el-row>			
			<el-col :span="24" class="toolbar">	
				<el-form label-width="120px">
					<el-form-item label="按站点名称搜索">
						<el-col :span="16">
							<el-form-item prop="date1">
								<!-- <el-input placeholder="请输入站点名称" v-model="filter_name" prefix-icon="el-icon-search" @change="searchBySiteName" clearable></el-input> -->
								<el-autocomplete style="width: 100%;" v-model="filter_name" :trigger-on-focus="true" :fetch-suggestions="querySearchAsync" placeholder="请输入站点名称" @select="handleSelect"></el-autocomplete>
							</el-form-item>
						</el-col>
						<el-col :span="4" style="padding-left: 20px;">
							<el-button v-show="!showMoreQuery" @click="showMoreQuery=true" type="default">更多搜索<i class="el-icon-arrow-down el-icon--right"></i></el-button>
							<el-button v-show="showMoreQuery"  @click="showMoreQuery=false" type="default">简单搜索<i class="el-icon-arrow-up el-icon--right"></i></el-button>
						</el-col>
					</el-form-item>					
					<el-form-item label="客户类型" v-show="showMoreQuery">
						<el-checkbox-group v-model="cutomerTypeList" @change="cutomerTypeChange">
							<el-checkbox label="Alpha" key="2"></el-checkbox>
							<el-checkbox label="Beta" key="1"></el-checkbox>
						</el-checkbox-group>
					</el-form-item>		
					<el-form-item label="站点状态" v-show="showMoreQuery">
						<el-checkbox-group>
							<el-checkbox label="正常" name="type"></el-checkbox>
							<el-checkbox label="报警" name="type"></el-checkbox>
							<el-checkbox label="离线" name="type"></el-checkbox>
							<el-checkbox label="待审批" name="type"></el-checkbox>							
						</el-checkbox-group>
					</el-form-item>										
				</el-form>					
			</el-col>	
		</el-row>
		<el-table :data="sites" style="width: 100%" :row-class-name="setSiteStatusRowClass" @sort-change="sortChange">
			<el-table-column prop="device_total" label="状态" :formatter="statusFormatter"></el-table-column>
			<el-table-column prop="customer_type" label="类型" :formatter="customerTypeFormatter" sortable="custom">
				<!-- <template slot-scope="scope">
        			<el-tag :type="scope.row.customer_type === 1 ? 'warning' : 'danger'" close-transition>
						{{scope.row.customer_type | customerTypeFilter}}
					</el-tag>
      			</template> -->
			</el-table-column>
			<el-table-column prop="parent_name" label="企业"></el-table-column>
			<el-table-column prop="name" label="站点" sortable="custom"> </el-table-column>
			<el-table-column prop="country" label="国家" sortable="custom" :formatter="countryFormatter"></el-table-column>			
			<el-table-column prop="device_online" label="AP数" sortable="custom"  :formatter="deviceNumFormatter"></el-table-column>
			<el-table-column prop="client_online" label="在线终端数" sortable="custom"></el-table-column>		
			<el-table-column prop="total_bytes" sortable="custom" label="日流量">
				<template slot-scope="scope">
					{{scope.row.total_bytes | sizeFilter}}
				</template>
			</el-table-column>
			<el-table-column prop="version" label="版本" :formatter="versionFormatter"></el-table-column>			
		</el-table>		
		<div class="footer">
			<el-pagination 			
				@current-change="handleCurrentChange"
				@size-change="handleSizeChange"
				:current-page="page"	
				:page-sizes="[10, 25, 50]"
				:page-size="page_size"				
				layout="total, sizes, prev, pager, next, jumper"
				:total="total">
			</el-pagination>
  		</div>		
	</section>	
</template>

<script>
	export default {
		data() {
			return {
				cutomerTypeList: [],
				showMoreQuery: false,
				filters: {
					name: ''
				},
				sites: [],
				listLoading: false,
				total: 0,
				page: 1,
				page_size: 10,
				sort: 'id desc',
				filter_cond: '',
				filter_name: '',
				filter_type: '',
				filter_status: ''
			}
		},
		methods: {	
			cutomerTypeChange(val){	
				this.page = 1;		
				if(val.length === 1){
					if(val[0] === 'Alpha'){
						this.filter_type = "customer_type=2";
					}else if(val[0] === 'Beta'){
						this.filter_type = "customer_type=1";
					}
				}else if(val.length === 2){
					this.filter_type = "customer_type=1 or customer_type=2";						
				}else{
					this.filter_type = "";
				}
				this.calculateFilter();
				this.getSites();
			},
			querySearchAsync(queryString, callback) {	
				var self = this;						
				this.$http.get('organizations/sites', { params: {				
					page_size : 10,				
					cond: "name like '%" + queryString +"%'"
				}}).then(res => {	
					res.data.list.forEach((item) => {
						item.value = item.name;
					})	
					if(res.data.list.length === 0){
						res.data.list.push({
							value: "没有搜索到结果, 点击选项显示所有站点信息",
							name: ''						
						})					
					}else{
						res.data.list.unshift({
							value: "点击选项显示所有站点信息",
							name: ''						
						})	
					}

					callback(res.data.list);				
				})
			},
			handleSelect(item) {
				this.filter_name = item.name;
				this.calculateFilter();
				this.getSites();
			},
			calculateFilter(){
				var conds = [];			
				if(this.filter_name.length != 0){
					conds.push("name like '%" + this.filter_name + "%'");
				}
				if(this.filter_type.length != 0){
					conds.push(this.filter_type);
				}		
				this.filter_cond = conds.join(' and ');	
				console.log("this.filter_cond", this.filter_cond);		
			},
			sortChange(sortParams){
				var order = "desc"
				if( sortParams.order === 'ascending' ){
					order = "asc";
				}

				if(sortParams.prop === null){
					sortParams.prop = "id";
				}
				this.sort = sortParams.prop + " " + order;
				this.getSites();
			},		
			setSiteStatusRowClass({row, rowIndex}){
				if(row.device_total === row.device_offline && row.device_total > 0){
					return 'warning-row';
				} 
				return '';
			},
      		handleCurrentChange(val) {
				this.page = val;
				this.getSites();
			},		
			handleSizeChange(val){
				this.page_size = val;
				this.getSites();
			},
			getSites() {			
				var self = this;			
				var params = {
					page : self.page,
					page_size : self.page_size,
					sort: self.sort,				
					cond: self.filter_cond
				};
				if(self.filter_cond.length === 0){
					delete params.cond;
				}
				this.listLoading = true;
				this.$http.get('organizations/sites', { params: params }).then(res => {
						this.total = res.data.total;
						this.sites = res.data.list;
						this.listLoading = false;
					})
					.catch(error => {
						this.listLoading = false;
						// this.$message.error(error);
					})
			},
			filterTag(value, row) {
				return row.customer_type === value;
			},
			countryFormatter(row, column) {
				var formatCountry = "未知";
				if(row.country === "CN"){
					formatCountry = "中国";
				}else if(row.country === "US"){
					formatCountry = "美国";
				}
        		return formatCountry;
			},
			statusFormatter(row, column){			
				if(row.device_total === row.device_offline && row.device_total > 0){
					return "离线";
				}

				if(row.device_offline > 0 && row.device_total > row.device_offline){
					return "告警";
				}

				return "正常";
			},
			customerTypeFormatter(row, column){
				var formatType = "未知";
				if(row.customer_type === 1){
					formatType = "Beta";
				}else if(row.customer_type === 2){
					formatType = "Alpha";
				}
				return formatType;				
			},		
			deviceNumFormatter(row, column){			
				return row.device_online + "/" + row.device_total;
			},
			trafficFormatter(row, column){
				return row.total_bytes;
			},
			versionFormatter(row, column){
				return "2.0.0";
			}
			  
		},
		mounted() {
			this.getSites();
		},
		filters:{
			customerTypeFilter(value){
				var formatType = "未知";
				if(value === 1){
					formatType = "Beta";
				}else if(value === 2){
					formatType = "Alpha";
				}
				return formatType;				
			},
            sizeFilter: function(bytes) {
                if (!bytes) return 0;
                if (bytes == 0) return "0 Bytes";
                var k = 1024,
                    sizes = ["Bytes", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB"],
                    i = Math.floor(Math.log(bytes) / Math.log(k));
                return parseFloat((bytes / Math.pow(k, i)).toFixed(0)) + " " + sizes[i];
            }					
		}		
	}
</script>

<style lang="scss">
	.el-form {
		width: 600px;
	}
	.footer{
		position: relative;
		margin-top: 20px;
	}
	.grid-content {
		border: 1px solid #ddd;
		min-height: 36px;
	}
	.el-table .warning-row {
		color: #fff;
		background: #F56C6C;
	}
</style>