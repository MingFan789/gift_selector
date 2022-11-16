# Gift Member-Target Selector Program

## setup Step

Create a resource folder with following file

config.yml

```yaml
env: UAT
mail:
  from: <From email>
  password: <Password>
  host: <Mail host>
  subject: <Mail Subject>
  template: <Template Path>
```

member_list.json

```json
{
    "member_list":{
        "<Member>": "<Email Address>"
    }
}
```