# Modelo genérico [o investidor]

**Dados:**
+ $C$: capital
+ $r_i$: rendimento do investimento $i = \{1, \ldots, n\}$
+ $\text{m}^\prime_i$: percentual mínimo do investimento $i = \{1, \ldots, n\}$
+ $\text{m}^{\prime\prime}_i$: percentual máximo do investimento $i = \{1, \ldots, n\}$

**Variáveis de decisão:**
+ $x_i$: valor indicado para o investimento $i = \{1, \ldots, n\}$

**Com isso, temos o modelo:**

$$
\begin{align} 
  \text{maximiza}\quad  &\sum_{i=1}^{n} r_i x_i \\
  \text{sujeito a}\quad &\sum_{i=1}^{n} x_i = C \\\\[.5em]
                        &x_j \ge m^\prime_j \left(\sum_{i=1}^n x_i\right),\quad j = \{1, \ldots, n\} \\\\[.5em]
                        &x_j \le m^{\prime\prime}_j \left(\sum_{i=1}^n x_i\right),\quad j = \{1, \ldots, n\} \\\\[.5em]
                        &x_i \ge 0,\quad i = \{1, \ldots, n\}
                          
\end{align} 
$$
