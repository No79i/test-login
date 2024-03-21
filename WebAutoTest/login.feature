Feature: 登录功能
    Scenario: 正常登录
      Given 我有一个开发方账号 用户名:huoyan 密码:P@ssw0rd

      When 打开登录页面 http://10.10.12.154:9901/
      And 输入用户名
      And 输入密码
      And 点击登录按钮

      Then 判断页面中是否有登出按钮
