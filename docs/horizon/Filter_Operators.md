# Filter Operators
## General syntax
### Comparison operators
```yaml
- <operator>:
    field: <field-reference> #Also see section below
    value: <expected value>
```

#### List of comparison operators
All operators return false when the specified field does not exist. Value can be of type `string`, `number`, `boolean`, or `array`. If the evaluated JSON-path is an object and not a field the operator returns false.

| Name             | Operator | Description                                               |
|------------------|----------|-----------------------------------------------------------|
| equal            | `eq`     | True if `field` == `value`.                               |
| regex            | `rx`     | True if `field` matches regex defined in `value`.         |
| not equal        | `ne`     | True if `field` != `value`.                               |
| less than        | `lt`     | True if `field` < `value`.                                |
| less or equal    | `le`     | True if `field` <= `value`.                               |
| greater than     | `gt`     | True if `field` >  `value`.                               |
| greater or equal | `ge`     | True if `field` >= `value`.                               |
| in               | `in`     | True if `field` is in `value` (of type array)             |
| contains         | `ct`     | True if `field` (of type array) contains `value`.         |
| does not contain | `nct`    | True if `field` (of type array) does not contain `value`. |

#### Field-reference (for JSON-payloads)
For the evaluation of the JSON-payload we support the [JSON-path-notation](https://github.com/json-path/JsonPath). Also filter within the path are allowed (also see [examples](#examples)).

| Operator                  | Description                                                  |
| :------------------------ | :----------------------------------------------------------- |
| `$`                       | The root element to query. This starts all path expressions. |
| `@`                       | The current node being processed by a filter predicate.      |
| `*`                       | Wildcard. Available anywhere a name or numeric are required. |
| `..`                      | Deep scan. Available anywhere a name is required.            |
| `.<name>`                 | Dot-notated child                                            |
| `['<name>' (, '<name>')]` | Bracket-notated child or children                            |
| `[<number> (, <number>)]` | Array index or indexes                                       |
| `[start:end]`             | Array slice operator                                         |

!!! important

    The filtering is always applied on the contents of the `data` field of an event message, not on the root of the whole event message. Therefore the nested field `data.foobar` will be referenced by `$.foobar` instead of `$.data.foobar`.

### Logical operators
```yaml
- <operator>:
    <list of logical or comparison-operators>
```

#### List of logical operators
| Name | Operator | Description                                                  |
| ---- | -------- | ------------------------------------------------------------ |
| or   | `or`     | True if **at least one** of the child-operators returns true |
| and  | `and`    | True if **all** of the child-operators return true           |

## Examples
### Example 1
```yaml
advancedSelectionFilter:
  and:
    - eq:
        field: $.processing.state
        value: IN_PROGRESS
    - or:
      - ge:
          field: $.total.amount
          value: 100000
      - eq:
          field: $.notify.policy
          value: ALWAYS
```

### Example 2
Advanced JSON-paths: Only send event when the quantity of the product with name "iPhone 13 Mini Black" is less than 10.
```yaml
advancedSelectionFilter:
  lt:
    field: $..product[?(@.name == "iPhone 13 Mini Black" )].quantity
    value: 10
```
The event with the payload below would be send to the consuming system since the quantity of available iPhones (2) is less than 10.
```json
{
  "stock": {
    "product": [
      {
        "name": "Samsung Galaxy S21",
        "quantity": 293
      },
      {
        "name": "iPhone 13 Mini Black",
        "quantity": 2
      }
    ]
  }
}
```
