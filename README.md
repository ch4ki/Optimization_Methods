# Nonlinear Programming: One-Dimensional Minimization Methods 
My Optimization Algorithms
The efficiency of an elimination method can be measured in terms of the ratio of the
final and the initial intervals of uncertainty, Ln/L0. The values of this ratio achieved
in various methods for a specified number of experiments (n = 5 and n = 10) are
compared in Table 5.3. It can be seen that the Fibonacci method is the most effi-
cient method, followed by the golden section method, in reducing the interval of
uncertainty.
A similar observation can be made by considering the number of experiments (or
function evaluations) needed to achieve a specified accuracy in various methods. The
results are compared in table for maximum permissible errors of 0.1 and 0.01. It
can be seen that to achieve any specified accuracy, the Fibonacci method requires the
least number of experiments, followed by the golden section method.

![Table](https://hizliresim.com/P79Yvl.png)
```python
import method_name
gdkq = method_name(objective_function,interval,accuracy)
gdkq.run() # returns 'optimal points'
```



## License
[MIT](https://choosealicense.com/licenses/mit/)
