# Idea Live Template
以下配置文件导入到Pycharm的live template的配置中

用于快速补全, 方便yaml文档的编写

> 持续完善中

```xml
<template name="200ok" value="200:&#10;  $ref: '#/responses/opt_success'" description="response  200 OK" toReformat="false" toShortenFQNames="true">
  <context>
    <option name="OTHER" value="true" />
  </context>
</template>
<template name="allof" value="allOf:&#10;  - $ref: '#/definitions/$END$'" description="allof" toReformat="false" toShortenFQNames="true">
  <context>
    <option name="OTHER" value="true" />
  </context>
</template>
<template name="def-array" value="$name$s:&#10;  description: $desc$&#10;  type: object&#10;  allOf:&#10;    - $ref: '#/definitions/array_base'&#10;    - type: object&#10;      properties:&#10;        data_list:&#10;          type: array&#10;          items:&#10;            $ref: '#/definitions/$name$'&#10;$END$" description="define array" toReformat="false" toShortenFQNames="true">
  <variable name="name" expression="" defaultValue="" alwaysStopAt="true" />
  <variable name="desc" expression="" defaultValue="" alwaysStopAt="true" />
  <context>
    <option name="OTHER" value="true" />
  </context>
</template>
<template name="def-obj" value="$name$:&#10;  type: object&#10;  description: $desc$&#10;  properties:&#10;    $END$" description="define object" toReformat="false" toShortenFQNames="true">
  <variable name="name" expression="" defaultValue="" alwaysStopAt="true" />
  <variable name="desc" expression="" defaultValue="" alwaysStopAt="true" />
  <context>
    <option name="OTHER" value="true" />
  </context>
</template>
<template name="delete" value="delete:&#10;  tags:&#10;    - $tag$&#10;  summary: $summary$&#10;  description: |&#10;    $desc$&#10;  parameters:&#10;    $param$&#10;  responses:&#10;    200:&#10;      $ref: '#/responses/opt_success'" description="delete" toReformat="false" toShortenFQNames="true">
  <variable name="tag" expression="" defaultValue="" alwaysStopAt="true" />
  <variable name="summary" expression="" defaultValue="" alwaysStopAt="true" />
  <variable name="desc" expression="" defaultValue="" alwaysStopAt="true" />
  <variable name="param" expression="" defaultValue="" alwaysStopAt="true" />
  <context>
    <option name="OTHER" value="true" />
  </context>
</template>
<template name="desc" value="description: $END$" description="description" toReformat="false" toShortenFQNames="true">
  <context>
    <option name="OTHER" value="true" />
  </context>
</template>
<template name="get" value="get:&#10;  tags:&#10;    - $tag$&#10;  summary: $summary$&#10;  description: |&#10;    $desc$&#10;  parameters:&#10;    $param$&#10;  responses:&#10;    200:&#10;      $ref: '#/responses/opt_success'" description="get" toReformat="false" toShortenFQNames="true">
  <variable name="tag" expression="" defaultValue="" alwaysStopAt="true" />
  <variable name="summary" expression="" defaultValue="" alwaysStopAt="true" />
  <variable name="desc" expression="" defaultValue="" alwaysStopAt="true" />
  <variable name="param" expression="" defaultValue="" alwaysStopAt="true" />
  <context>
    <option name="OTHER" value="true" />
  </context>
</template>
<template name="param" value="parameters:&#10;  $END$" description="parameters" toReformat="false" toShortenFQNames="true">
  <context>
    <option name="OTHER" value="true" />
  </context>
</template>
<template name="param-f-str" value="$name$_f:&#10;  in: formData&#10;  name: $name$&#10;  description: $desc$&#10;  type: string&#10;$END$" description="formData parameter string" toReformat="false" toShortenFQNames="true">
  <variable name="name" expression="" defaultValue="" alwaysStopAt="true" />
  <variable name="desc" expression="" defaultValue="" alwaysStopAt="true" />
  <context>
    <option name="OTHER" value="true" />
  </context>
</template>
<template name="param-q-str" value="$name$_q:&#10;  in: query&#10;  name: $name$&#10;  description: $desc$&#10;  type: string&#10;$END$" description="query parameter string" toReformat="false" toShortenFQNames="true">
  <variable name="name" expression="" defaultValue="" alwaysStopAt="true" />
  <variable name="desc" expression="" defaultValue="" alwaysStopAt="true" />
  <context>
    <option name="OTHER" value="true" />
  </context>
</template>
<template name="post" value="post:&#10;  tags:&#10;    - $tag$&#10;  summary: $summary$&#10;  description: |&#10;    $desc$&#10;  parameters:&#10;    $param$&#10;  responses:&#10;    200:&#10;      $ref: '#/responses/opt_success'" description="post" toReformat="false" toShortenFQNames="true">
  <variable name="tag" expression="" defaultValue="" alwaysStopAt="true" />
  <variable name="summary" expression="" defaultValue="" alwaysStopAt="true" />
  <variable name="desc" expression="" defaultValue="" alwaysStopAt="true" />
  <variable name="param" expression="" defaultValue="" alwaysStopAt="true" />
  <context>
    <option name="OTHER" value="true" />
  </context>
</template>
<template name="put" value="put:&#10;  tags:&#10;    - $tag$&#10;  summary: $summary$&#10;  description: |&#10;    $desc$&#10;  parameters:&#10;    $param$&#10;  responses:&#10;    200:&#10;      $ref: '#/responses/opt_success'" description="put" toReformat="false" toShortenFQNames="true">
  <variable name="tag" expression="" defaultValue="" alwaysStopAt="true" />
  <variable name="summary" expression="" defaultValue="" alwaysStopAt="true" />
  <variable name="desc" expression="" defaultValue="" alwaysStopAt="true" />
  <variable name="param" expression="" defaultValue="" alwaysStopAt="true" />
  <context>
    <option name="OTHER" value="true" />
  </context>
</template>
<template name="refd" value="$ref: '#/definitions/$END$'" description="define ref" toReformat="false" toShortenFQNames="true">
  <context>
    <option name="OTHER" value="true" />
  </context>
</template>
<template name="refp" value="$ref: '#/parameters/$END$'" description="param ref" toReformat="false" toShortenFQNames="true">
  <context>
    <option name="OTHER" value="true" />
  </context>
</template>
<template name="rsp" value="responses:&#10;  $END$" description="responses" toReformat="false" toShortenFQNames="true">
  <context>
    <option name="OTHER" value="true" />
  </context>
</template>
<template name="rsp-def" value="$name$:&#10;  description: $desc$&#10;  schema:&#10;    $ref: '#/definitions/$name$'&#10;    $END$" description="response define" toReformat="false" toShortenFQNames="true">
  <variable name="name" expression="" defaultValue="" alwaysStopAt="true" />
  <variable name="desc" expression="" defaultValue="" alwaysStopAt="true" />
  <context>
    <option name="OTHER" value="true" />
  </context>
</template>
```