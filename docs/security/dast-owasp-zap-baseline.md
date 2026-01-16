# DAST: OWASP ZAP Baseline Scan

This page explains the **DAST OWASP Baseline Scan** used in our CI pipeline.  
It helps you understand what DAST is, why we use OWASP ZAP, and what kinds of security issues it checks for.

---

## What is DAST?

DAST stands for **Dynamic Application Security Testing**.  
It tests your application **while it is running**, simulating how an attacker would interact with it from the outside.

DAST does *not* look at your source code.  
Instead, it scans the live application for security weaknesses such as:

- **Missing security headers**  
- **Weak cookies**  
- **Cross‑Site Scripting (XSS)**  
- **Cross‑Site Request Forgery (CSRF)**  
- **Open redirects**  
- **Session handling issues**  
- **Content Security Policy (CSP) problems**  

---

## What is OWASP ZAP?

OWASP ZAP (Zed Attack Proxy) is a free, open‑source security scanner maintained by the **Open Web Application Security Project**.

The **Baseline Scan** is a safe, non‑aggressive scan that:

- **Does not attack or fuzz your app**  
- **Checks for missing headers**  
- **Checks for common misconfigurations**  
- **Crawls your site to discover pages**  
- **Reports potential vulnerabilities**  

It is perfect for CI pipelines because it is:

- **Fast**  
- **Safe**  
- **Repeatable**  
- **Beginner‑friendly**  

---

## What the Baseline Scan Tests For

OWASP ZAP Baseline checks for:

### Security Headers
- **Content Security Policy (CSP)**  
- **X‑Frame‑Options**  
- **X‑Content‑Type‑Options**  
- **Strict‑Transport‑Security (HSTS)**  
- **Referrer‑Policy**  

### Cookie Security
- **Missing Secure flag**  
- **Missing HttpOnly flag**  
- **Missing SameSite flag**  

### Application Behaviour
- **Cross‑Site Scripting (XSS)**  
- **Open redirects**  
- **Mixed content**  
- **Insecure forms**  

---

## Why We Use It

The Baseline Scan helps you:

- **Understand real‑world security issues**  
- **See how attackers view your app**  
- **Learn secure defaults**  
- **Build confidence in deploying secure software**  

It is a core part of modern DevSecOps practice.

---
