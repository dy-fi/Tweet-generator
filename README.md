# Tweet-generator

## A Tweet gen/flask site
<ul>
<li> written in Python Flask with render_templates and a markov chain </li>
<li> in developement </li>
</ul>

<hr>
## source scripts analyzer
#### /scripts/source scripts analyzer
This is a simple script for getting the lower level of code inside of python,
for achieving O(1) lookup time for [arbitrary indexes in dictionaries](https://www.oreilly.com/library/view/high-performance-python/9781449361747/ch04.html)
Don't actually use the code they used in your stuff though

```
import inspect
lines = inspect.getsource('')
print(lines)
```

### How to use
put anything inside the ''
