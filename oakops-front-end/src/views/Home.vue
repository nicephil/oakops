<template>
	<el-row class="container">
		<el-col :span="24" class="header">
			<el-col :span="10" class="logo" :class="collapsed?'logo-collapse-width':'logo-width'">
				{{collapsed?'':sysName}}
			</el-col>
			<el-col :span="10">
				<div class="tools" @click.prevent="collapse">
					<!-- <i class="fa fa-align-justify"></i> -->
				</div>
			</el-col>
			<el-col :span="4" class="userinfo">
				<el-dropdown trigger="hover">
					<span class="el-dropdown-link userinfo-inner">{{sysUserName}}</span>
					<el-dropdown-menu slot="dropdown">
						<!-- <el-dropdown-item>我的消息</el-dropdown-item> -->
						<el-dropdown-item>设置</el-dropdown-item>
						<el-dropdown-item divided @click.native="logout">退出登录</el-dropdown-item>
					</el-dropdown-menu>
				</el-dropdown>
			</el-col>
		</el-col>
		<el-col :span="24" class="main">
			<el-col :span="24" class="content-wrapper">
				<transition name="fade" mode="out-in">
					<router-view></router-view>
				</transition>
			</el-col>	
		</el-col>
	</el-row>
</template>

<script>
	export default {
		data() {
			return {
				sysName: 'Oakridge Operation',
				collapsed: false,
				sysUserName: '',
				sysUserAvatar: '',
				form: {
					name: '',
					region: '',
					date1: '',
					date2: '',
					delivery: false,
					type: [],
					resource: '',
					desc: ''
				}
			}
		},
		methods: {
			handleselect: function(a, b) {},
			//退出登录
			logout: function() {
				var _this = this;
				this.$confirm('确认退出吗?', '提示', {
					//type: 'warning'
				}).then(() => {
					this.$http.post('logout').then(res =>{
						sessionStorage.removeItem('user');
						_this.$router.push('/login');
					})
				}).catch(() => {
				});
			},
			//折叠导航栏
			collapse: function() {
				this.collapsed = !this.collapsed;
			},
			showMenu(i, status) {
				this.$refs.menuCollapsed.getElementsByClassName('submenu-hook-' + i)[0].style.display = status ? 'block' : 'none';
			}
		},
		mounted() {
			var user = sessionStorage.getItem('user');
			if (user) {
				user = JSON.parse(user);
				this.sysUserName = user.username || 'Unknow';
			}
		}
	}
</script>

<style lang="scss">
	@import '~scss_vars';
	.container {
		position: absolute;
		top: 0px;
		bottom: 0px;
		width: 100%;
		.header {
			height: 60px;
			line-height: 60px;
			background: $color-primary;
			color: #fff;
			.userinfo {
				text-align: right;
				padding-right: 35px;
				float: right;
				.userinfo-inner {
					cursor: pointer;
					color: #fff;
					img {
						width: 40px;
						height: 40px;
						border-radius: 20px;
						margin: 10px 0px 10px 10px;
						float: right;
					}
				}
			}
			.logo {
				//width:230px;
				height: 60px;
				font-size: 22px;
				padding-left: 20px;
				padding-right: 20px;
				border-color: rgba(238, 241, 146, 0.3);
				border-right-width: 0;
				border-right-style: solid;
				img {
					width: 40px;
					float: left;
					margin: 10px 10px 10px 18px;
				}
				.txt {
					color: #fff;
				}
			}
			.logo-width {
				width: 230px;
			}
			.logo-collapse-width {
				width: 60px
			}
			.tools {
				padding: 0px 23px;
				width: 14px;
				height: 60px;
				line-height: 60px;
				cursor: pointer;
			}
		}
		.main {
			display: flex; // background: #324057;
			position: absolute;
			top: 60px;
			bottom: 0px;
			overflow: hidden;
			.content-wrapper {
				background-color: #fff;
				box-sizing: border-box;
				display: flex;
				position: absolute;
				top: 0;
				bottom: 0;
				overflow: hidden;					
			}
		}
	}
</style>