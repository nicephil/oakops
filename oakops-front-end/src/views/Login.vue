<template>
 <div class="loginBg">
  <el-form :model="ruleForm2" :rules="rules2" ref="ruleForm2" label-position="left" label-width="0px" class="demo-ruleForm login-container">
    <h3 class="title">Oakridge运控平台</h3>
    <el-form-item prop="account">
      <el-input type="text" v-model="ruleForm2.account" auto-complete="off" placeholder="账号"></el-input>
    </el-form-item>
    <el-form-item prop="checkPass">
      <el-input type="password" v-model="ruleForm2.checkPass" auto-complete="off" placeholder="密码"></el-input>
    </el-form-item>
    <!-- <el-checkbox v-model="checked" checked class="remember">记住密码</el-checkbox> -->
    <el-form-item style="width:100%;">
      <el-button type="primary" style="width:100%;" @click.native.prevent="handleSubmit2" :loading="logining">登录</el-button>
      <!--<el-button @click.native.prevent="handleReset2">重置</el-button>-->
    </el-form-item>
  </el-form>
</div>
</template>

<script>
  export default {
    data() {
      return {     
        logining: false,
        ruleForm2: {
          account: '',
          checkPass: ''
        },
        rules2: {
          account: [{
              required: true,
              message: '请输入账号',
              trigger: 'blur'
            },
            //{ validator: validaePass }
          ],
          checkPass: [{
              required: true,
              message: '请输入密码',
              trigger: 'blur'
            },
            //{ validator: validaePass2 }
          ]
        },
        checked: true
      };
    },
    mounted: function() {
      // console.log("Mounted")
    },
    methods: {
      handleReset2() {
        this.$refs.ruleForm2.resetFields();
      },
      handleSubmit2(ev) {
        var self = this;
        self.$refs.ruleForm2.validate((valid) => {
          if (valid) {
            //_this.$router.replace('/table');
            self.logining = true;
            //NProgress.start();
            var loginParams = {
              username: self.ruleForm2.account,
              password: self.ruleForm2.checkPass
            };
            this.$http.post('login', loginParams)
              .then(res => {        
                self.logining = false; 
                sessionStorage.setItem('user', JSON.stringify({
                  username: loginParams.username,
                  access_token: res.data.access_token,
                  refresh_token: res.data.refresh_token
                }));

                var item = sessionStorage.getItem('user')

                self.$router.push({
                  path: '/organization'
                });                              
              })
              .catch(error => {                
                self.logining = false; 
                if(error.data.error_message){
                  this.$message.error("用户名或者密码不正确，请核对后重试!");
                }else{
                  this.$message.error("登录失败, 请重试!");
                }
                
              })            
          } else {          
            return false;
          }
        });
      }
    }
  }
</script>

<style lang="scss" scoped>
  .login-container {
    /*box-shadow: 0 0px 8px 0 rgba(0, 0, 0, 0.06), 0 1px 0px 0 rgba(0, 0, 0, 0.02);*/
    -webkit-border-radius: 5px;
    border-radius: 5px;
    -moz-border-radius: 5px;
    background-clip: padding-box;
    margin: 180px auto;
    width: 350px;
    padding: 35px 35px 15px 35px;
    background: #fff;
    border: 1px solid #eaeaea;
    box-shadow: 0 0 25px #cac6c6;
    .title {
      margin: 0px auto 40px auto;
      text-align: center;
      color: #505458;
    }
    .remember {
      margin: 0px 0px 35px 0px;
    }
  }
</style>