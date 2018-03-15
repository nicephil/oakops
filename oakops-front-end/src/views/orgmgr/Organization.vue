<template>
	<section>
		<el-col :span="24" class="toolbar" style="padding-bottom: 0px;">
			<el-form :inline="true" :model="filters">
				<el-form-item>
					<el-input v-model="filters.name" placeholder="站点名称"></el-input>
				</el-form-item>
				<el-form-item>
					<el-button type="primary">查询</el-button>
				</el-form-item>
			</el-form>
		</el-col>
		<el-col :span="24" class="companyList">
			<el-table :data="organizations" style="width: 100%" :show-header="false">
				<el-table-column type="expand">
					<template slot-scope="props">
						<el-table  :data="props.row.children" border style="width: 100%">
							<el-table-column prop="name" label="名称" width="180"></el-table-column>
							<el-table-column prop="country" label="国家" width="180"></el-table-column>
							<el-table-column prop="zone_id" label="时区"> </el-table-column>
						</el-table>
					</template>
    			</el-table-column>
    			<el-table-column>
					<template slot-scope="props">
						<span>{{props.row.name}}</span>
						<el-tag v-if="props.row.customer_type === 1" :closable="false" size="mini" type="warning">Beta</el-tag>                                    
                        <el-tag v-if="props.row.customer_type === 2" :closable="false" size="mini" type="danger">Alpha</el-tag>						
					</template>					
				</el-table-column>				
  			</el-table>
		</el-col>
	</section>
</template>

<script>
	export default {
		data() {
			return {
				filters: {
					name: ''
				},
				organizations: [],
				listLoading: false,
				total: 0,
				page: 1,
			}
		},
		methods: {
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
			}
		},
		mounted() {
			this.getOrganizations();
		}
	}
</script>

<style lang="scss" scoped>

</style>