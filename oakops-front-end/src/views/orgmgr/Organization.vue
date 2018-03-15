<template>
	<section>
		<el-row>			
			<el-col :span="24" class="toolbar">	
				<el-form label-width="120px">
					<el-form-item label="按站点名称搜索">
						<el-col :span="16">
							<el-form-item prop="date1">
								<el-input placeholder="请输入内容" prefix-icon="el-icon-search"></el-input>
							</el-form-item>
						</el-col>
						<el-col :span="4" style="padding-left: 20px;">
							<el-button v-show="!showMoreQuery" @click="showMoreQuery=true" type="default">更多搜索<i class="el-icon-arrow-down el-icon--right"></i></el-button>
							<el-button v-show="showMoreQuery"  @click="showMoreQuery=false" type="default">简单搜索<i class="el-icon-arrow-up el-icon--right"></i></el-button>
						</el-col>
					</el-form-item>					
					<el-form-item label="客户类型" v-show="showMoreQuery">
						<el-checkbox-group>
							<el-checkbox label="Alpha" name="type"></el-checkbox>
							<el-checkbox label="Beta" name="type"></el-checkbox>
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
		<el-table :data="tableData" style="width: 100%" :default-sort = "{prop: 'date', order: 'descending'}">
			<el-table-column prop="date" label="日期" sortable width="180"></el-table-column>
			<el-table-column prop="name" label="姓名" sortable width="180"> </el-table-column>
			<el-table-column prop="address" label="地址" :formatter="formatter"></el-table-column>
		</el-table>		
		<div class="footer">
			<el-pagination 
				@size-change="handleSizeChange"
				@current-change="handleCurrentChange"
				:current-page="1"
				:page-sizes="[25, 50, 100]"
				:page-size="25"
				layout="total, sizes, prev, pager, next, jumper"
				:total="400">
			</el-pagination>
  		</div>		
	</section>	
</template>

<script>
	export default {
		data() {
			return {
				showMoreQuery: false,
				filters: {
					name: ''
				},
				organizations: [],
				listLoading: false,
				total: 0,
				page: 1,
				tableData: [{
						date: '2016-05-02',
						name: '王小虎',
						address: '上海市普陀区金沙江路 1518 弄'
					}, {
						date: '2016-05-04',
						name: '王小虎',
						address: '上海市普陀区金沙江路 1517 弄'
					}, {
						date: '2016-05-01',
						name: '王小虎',
						address: '上海市普陀区金沙江路 1519 弄'
					}, {
						date: '2016-05-03',
						name: '王小虎',
						address: '上海市普陀区金沙江路 1516 弄'
					},
					{
						date: '2016-05-02',
						name: '王小虎',
						address: '上海市普陀区金沙江路 1518 弄'
					}, {
						date: '2016-05-04',
						name: '王小虎',
						address: '上海市普陀区金沙江路 1517 弄'
					}, {
						date: '2016-05-01',
						name: '王小虎',
						address: '上海市普陀区金沙江路 1519 弄'
					}, {
						date: '2016-05-03',
						name: '王小虎',
						address: '上海市普陀区金沙江路 1516 弄'
					},
					{
						date: '2016-05-02',
						name: '王小虎',
						address: '上海市普陀区金沙江路 1518 弄'
					}, {
						date: '2016-05-04',
						name: '王小虎',
						address: '上海市普陀区金沙江路 1517 弄'
					}, {
						date: '2016-05-01',
						name: '王小虎',
						address: '上海市普陀区金沙江路 1519 弄'
					}, {
						date: '2016-05-03',
						name: '王小虎',
						address: '上海市普陀区金沙江路 1516 弄'
					},
					{
						date: '2016-05-02',
						name: '王小虎',
						address: '上海市普陀区金沙江路 1518 弄'
					}, {
						date: '2016-05-04',
						name: '王小虎',
						address: '上海市普陀区金沙江路 1517 弄'
					}, {
						date: '2016-05-01',
						name: '王小虎',
						address: '上海市普陀区金沙江路 1519 弄'
					}, {
						date: '2016-05-03',
						name: '王小虎',
						address: '上海市普陀区金沙江路 1516 弄'
					}
				]
			}
		},
		methods: {
 			handleSizeChange(val) {
        		console.log(`每页 ${val} 条`);
      		},
      		handleCurrentChange(val) {
        		console.log(`当前页: ${val}`);
      		},			
			getOrganizations() {
				this.listLoading = true;
				this.$http.get('organizations').then(res => {
						this.total = res.data.total;
						this.organizations = res.data.list;
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
			formatter(row, column) {
        		return row.address;
      		}
		},
		mounted() {
			this.getOrganizations();
		}
	}
</script>

<style lang="scss" scoped>
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
</style>