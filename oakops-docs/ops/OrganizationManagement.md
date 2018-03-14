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
URI: /ops/v1/organizations
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
|customer_type|int||
|children|List|children group nodes|

###示例

#### 请求示例

```
http:/ops.oakridge.io/ops/v1/organizations
```

#### 返回示例
body

```
{
  "list": [
    {
      "zone_id": null,
      "country": "CN",
      "children": [
        {
          "zone_id": "Asia/Shanghai",
          "country": "CN",
          "children": [
            
          ],
          "parent_id": 2,
          "customer_type": 1,
          "address": "杭州市",
          "id": 3,
          "name": "Oak-xxia-hz"
        },
        {
          "zone_id": "Asia/Shanghai",
          "country": "CN",
          "children": [
            
          ],
          "parent_id": 2,
          "customer_type": 2,
          "address": "大星海纯k.高新店",
          "id": 32,
          "name": "Oak-xxia-test1"
        }
      ],
      "parent_id": 1,
      "customer_type": 1,
      "id": 2,
      "name": "Oak-xxia"
    },
    {
      "zone_id": null,
      "country": "CN",
      "children": [
        {
          "zone_id": "Asia/Shanghai",
          "country": "CN",
          "children": [
            
          ],
          "parent_id": 33,
          "customer_type": 2,
          "address": "红河哈尼族彝族自治州",
          "id": 34,
          "name": "hh-oak-hz"
        }
      ],
      "parent_id": 1,
      "customer_type": 2,
      "id": 33,
      "name": "hh-oak-hz"
    },
    {
      "zone_id": null,
      "country": "CN",
      "children": [
        {
          "zone_id": "Asia/Shanghai",
          "country": "CN",
          "children": [
            
          ],
          "parent_id": 49,
          "customer_type": 2,
          "address": "爱丝特(esther)甜品烘焙",
          "id": 50,
          "name": "test"
        }
      ],
      "parent_id": 1,
      "customer_type": 2,
      "id": 49,
      "name": "test"
    }
  ],
  "error_code": 0
}
```