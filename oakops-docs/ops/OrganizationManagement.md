# 目录
[**1. 组织**](#organization)<br>
[**1.1 获取组织列表**](#organization-list)<br>

# <a name="organization"></a>1.组织

## <a name="organization-list"></a>1.1 获取站点列表

###描述
获取站点的信息列表

###类型
```
http method: GET
URI: /ops/v1/organizations/sites
```

### 请求参数
```
```
Parameter:

|Name|Required|Type|Description|
|:---|:-------|:---|:----------|
|page|N|int|page number, default is 1|
|page_size|N|int|page size, default is 10|
|search|String||
|sort|N|String|sort key, support **asc** and **desc**, such as **id asc**;  **id desc,name desc**<br>support key:|
|status|int[]|0 : normal<br>1 : alert<br>2 : offline|
|customer_types|int[]||



### 返回结果
```
Format: application/json
```
Result:

|Name|Type|Description|
|:---|:---|:----------|
|error_code|int|error code|
|error_message|String|error message|
|total|int|total number|
|list|List|sites list|

#### site info

|Name|Type|Description|
|:---|:---|:----------|
|id|long||
|name|String||
|address|String||
|country|String||
|zond_id|String||
|parent_id|long|parent id|
|parent_name|String||
|customer_type|int||
|client_online|int|onlien client number|
|device_total|int|total device number|
|device_online|int|online device number|
|device_offline|int|offline device number|
|device_unused|int|unused device number|
|total_bytes|long||
|status|int||
|owner|String||
|nms|String||



###示例

#### 请求示例

```
http:/ops.oakridge.io/ops/v1/organizations/sites
```

#### 返回示例
body

```
{
  "error_code": 0,
  "list": [
    {
      "device_total": 2,
      "device_offline": 0,
      "zone_id": "Asia/Shanghai",
      "parent_name": "Oak-xxia",
      "country": "CN",
      "device_unused": 0,
      "name": "Oak-xxia-hz",
      "parent_id": 2,
      "customer_type": 1,
      "total_bytes": 0,
      "address": "杭州市",
      "client_online": 1,
      "id": 3,
      "device_online": 2
    },
    {
      "device_total": 0,
      "device_offline": 0,
      "zone_id": "Asia/Shanghai",
      "parent_name": "Oak-xxia",
      "country": "CN",
      "device_unused": 0,
      "name": "Oak-xxia-test1",
      "parent_id": 2,
      "customer_type": 2,
      "total_bytes": 0,
      "address": "大星海纯k.高新店",
      "client_online": 0,
      "id": 32,
      "device_online": 0
    },
    {
      "device_total": 0,
      "device_offline": 0,
      "zone_id": "Asia/Shanghai",
      "parent_name": "hh-oak-hz",
      "country": "CN",
      "device_unused": 0,
      "name": "hh-oak-hz",
      "parent_id": 33,
      "customer_type": 2,
      "total_bytes": 0,
      "address": "红河哈尼族彝族自治州",
      "client_online": 0,
      "id": 34,
      "device_online": 0
    },
    {
      "device_total": 0,
      "device_offline": 0,
      "zone_id": "Asia/Shanghai",
      "parent_name": "test",
      "country": "CN",
      "device_unused": 0,
      "name": "test",
      "parent_id": 49,
      "customer_type": 2,
      "total_bytes": 0,
      "address": "爱丝特(esther)甜品烘焙",
      "client_online": 0,
      "id": 50,
      "device_online": 0
    }
  ]
}
```