> This release of ExpreesJS no longer supports "sub-expression" regular expressions. 
> For example `/:foo(\\d+)`

---
[Refer this](https://owasp.org/www-community/attacks/Regular_expression_Denial_of_Service_-_ReDoS)

---
# What is **ReDOS**
- The **Regular expression Denial of Service (ReDoS)** is a [Denial of Service](https://owasp.org/www-community/attacks/Denial_of_Service) attack, that exploits the fact that most Regular Expression implementations may reach extreme situations that cause them to work very slowly (exponentially related to input size).
- An attacker can then cause a program using a Regular Expression (Regex) to enter these extreme situations and then hang for a very long time.

---
