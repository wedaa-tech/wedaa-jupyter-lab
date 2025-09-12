# 📘 Differentiation & Integration Basics (Cheat-Sheet)

This sheet covers the **core rules, formulas, and applications** of differentiation and integration, especially for **Data Science & Probability**.

---

## 🔹 Differentiation

👉 **Definition:** Rate of change / slope of a function.  
If \(y = f(x)\), derivative is:  
\[
\frac{dy}{dx} \quad \text{or} \quad f'(x)
\]

### **Rules**
1. Constant: \(\frac{d}{dx}(c) = 0\)
2. Power: \(\frac{d}{dx}(x^n) = n x^{n-1}\)
3. Constant multiple: \(\frac{d}{dx}[c f(x)] = c f'(x)\)
4. Sum: \(\frac{d}{dx}[f(x)+g(x)] = f'(x)+g'(x)\)
5. Product: \((fg)' = f'g + fg'\)
6. Quotient: \(\big(\frac{f}{g}\big)' = \frac{f'g - fg'}{g^2}\)
7. Chain: If \(y=f(g(x))\), then \(dy/dx = f'(g(x)) g'(x)\)

### **Common Derivatives**
- \(\frac{d}{dx}(x) = 1\)
- \(\frac{d}{dx}(x^n) = n x^{n-1}\)
- \(\frac{d}{dx}(e^x) = e^x\)
- \(\frac{d}{dx}(\ln x) = 1/x\)
- \(\frac{d}{dx}(\sin x) = \cos x\)
- \(\frac{d}{dx}(\cos x) = -\sin x\)
- \(\frac{d}{dx}(\tan x) = \sec^2 x\)

### **Applications in Data Science**
- Gradient Descent (optimization)
- Finding maxima/minima (critical points)
- Sensitivity analysis

---

## 🔹 Integration

👉 **Definition:** Reverse of differentiation; gives accumulated area under a curve.  
If \(F'(x) = f(x)\), then:  
\[
\int f(x) dx = F(x) + C
\]

### **Rules**
1. Constant: \(\int c dx = cx + C\)
2. Power: \(\int x^n dx = \frac{x^{n+1}}{n+1} + C, \; n \neq -1\)
3. Sum: \(\int [f(x)+g(x)] dx = \int f(x) dx + \int g(x) dx\)
4. Constant multiple: \(\int cf(x) dx = c \int f(x) dx\)

### **Common Integrals**
- \(\int x^n dx = \frac{x^{n+1}}{n+1} + C\)
- \(\int e^x dx = e^x + C\)
- \(\int 1/x dx = \ln|x| + C\)
- \(\int \sin x dx = -\cos x + C\)
- \(\int \cos x dx = \sin x + C\)
- \(\int \sec^2 x dx = \tan x + C\)

### **Applications in Data Science**
- Probability density functions (PDFs):  
  \(P(a \leq X \leq b) = \int_a^b f(x) dx\)
- Cumulative distribution function (CDF):  
  \(F(x) = \int_{-\infty}^x f(t) dt\)
- Expectation (mean):  
  \(E[X] = \int_{-\infty}^{\infty} x f(x) dx\)
- Variance:  
  \(Var(X) = E[X^2] - (E[X])^2\)

---

## 🔗 Relationship (Fundamental Theorem of Calculus)
- Differentiation and Integration are **inverse operations**:
  - \(\frac{d}{dx}\left(\int f(x) dx\right) = f(x)\)
  - \(\int f'(x) dx = f(x) + C\)
- Area under curve = change in antiderivative:  
  \(\int_a^b f(x) dx = F(b) - F(a)\)

---

## 📊 Worked Examples

### Example 1: Basic Derivative
Find \(\frac{d}{dx}(x^3)\):
\[
\frac{d}{dx}(x^3) = 3x^2
\]

### Example 2: Basic Integral
Find \(\int x dx\):
\[
\int x dx = \frac{x^2}{2} + C
\]

### Example 3: Probability Density Function (PDF)
For Uniform distribution on [0,1], PDF is:
\[
f(x) = 1, \quad 0 \leq x \leq 1
\]
Probability that \(X\) lies between 0.2 and 0.5:
\[
P(0.2 \leq X \leq 0.5) = \int_{0.2}^{0.5} 1 dx = (0.5 - 0.2) = 0.3
\]

### Example 4: Cumulative Distribution Function (CDF)
For the same Uniform(0,1),
\[
F(x) = \int_0^x 1 dt = x, \quad 0 \leq x \leq 1
\]
So, \(F(0.7) = 0.7\).

### Example 5: Expectation of Normal Distribution
For standard Normal(0,1):
\[
E[X] = \int_{-\infty}^{\infty} x \cdot \frac{1}{\sqrt{2\pi}} e^{-x^2/2} dx = 0
\]
(Symmetric function → mean is 0)

---

✅ Use this sheet for **exam prep & intuition**: 
- Derivative = *slope* 
- Integral = *area*  
Both are essential for **Data Science & Probability**.

