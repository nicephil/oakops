# 目录
[**1. 组织**](#organization)<br>
[**1.1 获取组织列表**](#organization-list)<br>

# <a name="organization"></a>1.组织

## <a name="organization-list"></a>1.1 获取组织列表

###描述
获取企业和站点的基本信息列表

###类型
```
http method: GET
URI: /ops/v1/organization
```

### 请求参数
```
```
Parameter:

|Name|Required|Type|Description|
|:---|:-------|:---|:----------|


### 返回结果
```
Format: application/json
```
Result:

|Name|Type|Description|
|:---|:---|:----------|
|error_code|int|error code|
|error_message|String|error message|
|list|List|organization list|

#### organizaiton info

|Name|Type|Description|
|:---|:---|:----------|
|id|long||
|name|String||
|address|String||
|country|String||
|zond_id|String||
|parent_id|long|parent id|
|children|List|children group nodes|
|customer_type|int||

###示例

#### 请求示例

```
http:/ops.oakridge.io/ops/v1/organization
```

#### 返回示例
body

```
{
}
```