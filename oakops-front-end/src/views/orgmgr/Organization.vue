<template>
	<el-container>
		<el-aside width="250px">
			<el-row>
				<el-col :span="24">				
					<el-menu :default-openeds="['1','2','3']">
						<el-submenu index="1">
							<template slot="title">							
								<span>按名称搜索</span>
							</template>
							<div class="search-item">
								<!-- <el-autocomplete style="width: 100%;" v-model="filter_name" :trigger-on-focus="true" :fetch-suggestions="querySearchAsync" placeholder="企业名/站点名/所有者" @select="handleSelect"></el-autocomplete> -->
								<el-input placeholder="企业名/站点名/所有者" v-model="search" class="input-with-select" @keyup.enter.native="nameSearchChange" clearable>									
									<el-button slot="append" class="append-btn" icon="el-icon-search" @click="nameSearchChange"></el-button>								
								</el-input>
							</div>							
						</el-submenu>		
						<el-submenu index="2">
							<template slot="title">							
								<span>站点状态过滤</span>
							</template>
							<el-menu-item-group>
								<el-checkbox-group v-model="statusList" @change="statusFilterChange">
									<div class="filter-item">
										<el-checkbox label="正常" key="normal"></el-checkbox>
									</div>
									<div class="filter-item">
										<el-checkbox label="报警"></el-checkbox>
									</div>
									<div class="filter-item">
										<el-checkbox label="离线"></el-checkbox>
									</div>
									<div class="filter-item">
										<el-checkbox label="待审批" disabled></el-checkbox>							
									</div>									
								</el-checkbox-group>							
							</el-menu-item-group>
						</el-submenu>
						<el-submenu index="3">
							<template slot="title">							
								<span>站点类型过滤</span>
							</template>
							<el-menu-item-group>
								<el-checkbox-group v-model="cutomerTypeList" @change="cutomerTypeChange">
									<div class="filter-item">
										<el-checkbox label="Alpha" key="2"></el-checkbox>
									</div>
									<div class="filter-item">
										<el-checkbox label="Beta" key="1"></el-checkbox>
									</div>								
								</el-checkbox-group>							
							</el-menu-item-group>
						</el-submenu>						
					</el-menu>
				</el-col>
			</el-row>			
		</el-aside>
		<el-main>
			<el-table :max-height="table_height" :data="sites" style="width: 100%" :row-class-name="setSiteStatusRowClass" @sort-change="sortChange" v-loading="listLoading">
				<el-table-column width="55" type="selection" fixed></el-table-column>				
				<el-table-column width="80" prop="status" label="状态" sortable="custom" :formatter="statusFormatter"></el-table-column>
				<el-table-column width="100" prop="customer_type" label="类型" :formatter="customerTypeFormatter" sortable="custom">
					<!-- <template slot-scope="scope">
						<el-tag :type="scope.row.customer_type === 1 ? 'warning' : 'danger'" close-transition>
							{{scope.row.customer_type | customerTypeFilter}}
						</el-tag>
					</template> -->
				</el-table-column>
				<el-table-column prop="parent_name" label="企业" sortable="custom"></el-table-column>
				<el-table-column prop="name" label="站点" sortable="custom"> </el-table-column>
				<el-table-column width="100"  prop="country" label="国家" sortable="custom" :formatter="countryFormatter"></el-table-column>			
				<el-table-column width="100"  prop="device_online" label="AP数" sortable="custom"  :formatter="deviceNumFormatter"></el-table-column>
				<el-table-column width="120" prop="client_online" label="在线终端数" sortable="custom"></el-table-column>		
				<el-table-column width="120" prop="total_bytes" sortable="custom" label="日流量">
					<template slot-scope="scope">
						{{scope.row.total_bytes | sizeFilter}}
					</template>
				</el-table-column>
				<el-table-column prop="owner" label="所有者" sortable="custom"></el-table-column>
				<el-table-column prop="nms" label="OakManager" sortable="custom"></el-table-column>			
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
		</el-main>		
	</el-container>
</template>

<script>
	import qs from "qs";
	export default {
		data() {
			return {	
				table_height:"100%",			
				cutomerTypeList: [],
				statusList: [],
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
				search: '',			
				filterStatus: [],
				filterCustomerType:[]
			}
		},
		methods: {	
			nameSearchChange(val){				
				this.getSites();				
			},	
			statusFilterChange(val){
				this.page = 1;
				var status = [];
				val.forEach(item => {
					if(item === '正常'){
						status.push(0);
					}
					if(item === '报警'){
						status.push(1);
					}				
					if(item === '离线'){
						status.push(2);
					}							
				})				
				this.filterStatus = status;
				this.getSites();				
			},
			cutomerTypeChange(val){	
				this.page = 1;		
				var types = [];
				val.forEach(item => {
					if(item === 'Alpha'){
						types.push(2);
					}
					if(item === 'Beta'){
						types.push(1);
					}					
				})				
				this.filterCustomerType = types;
				this.getSites();
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
					search: self.search,	
					status: self.filterStatus,
					customer_types: self.filterCustomerType					
				};			
				this.listLoading = true;
				this.$http.get('organizations/sites', { 
					params: params,
					paramsSerializer: function(params) {
       					return qs.stringify(params, {arrayFormat: 'repeat'})
    				}}).then(res => {
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
				switch(row.country){
					case "CN":return "中国";
					case "US":return "美国";								
					default: return "未知";
				}
			},
			statusFormatter(row, column){		
				switch(row.status){
					case 0:return "正常";
					case 1:return "报警";
					case 2:return "离线";					
					default: return "未知";
				}
			},
			customerTypeFormatter(row, column){
				switch(row.customer_type){
					case 1:return "Beta";
					case 2:return "Alpha";								
					default: return "未知";
				}			
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
			this.table_height = document.documentElement.clientHeight - 150;
			// console.log("window.innerHeight", window.innerHeight);
			// console.log("document.documentElement.clientHeight", document.documentElement.clientHeight);
			// console.log("document.body.clientHeight", document.body.clientHeight);
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
	.el-aside {	
		border-right: 1px solid #e6e6e6;
		list-style: none;
		position: relative;		
		margin: 0;
		padding: 20px 0 0 0;
		background-color: #fff;
		.el-menu{
			border-right: none;
		}
		.filter-item{
			padding: 0 20px 20px 20px;
		}		
		.search-item{
			padding: 10px 20px 20px 20px;
			.el-input-group__append{
				background: transparent;
				padding: 0 3px;
			}
		}	
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
		background: oldlace;
	}

</style>