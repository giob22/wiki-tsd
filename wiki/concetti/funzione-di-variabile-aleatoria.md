---
tipo: concetto
importanza_esame: media
prerequisiti: ["variabile-aleatoria"]
fonti_pdf: ["Probabilità.pdf#page=27"]
---

# Funzione di una variabile aleatoria

## Definizione

> 📄 Fonte: [[Probabilità.pdf#page=27]]

Se $X$ è una v.a. e $g$ una funzione reale, $Y = g(X)$ è a sua volta una v.a. La sua CDF si ricava dalla definizione:
$$F_Y(y) = P\big(\{\omega\in\Omega : g(X(\omega))\le y\}\big)$$

> ⚠️ Contraddizione (refuso nelle slide): la slide scrive "$g(X(\omega)) \le x$". L'argomento corretto è $y$.

## Formule

> 🧮 Formula chiave ([[Probabilità.pdf#page=27]]): se $y=g(x)$ ha un numero finito di soluzioni $x_i$ e in ciascuna $g'(x_i)$ esiste ed è $\neq 0$,
> $$f_Y(y) = \sum_i \frac{f_X(x_i)}{|g'(x_i)|}$$

Simboli: $x_i = x_i(y)$ radici di $g(x)=y$; $g'$ derivata di $g$.

Caso affine $Y = aX+b$ con $X\sim\mathcal{N}(0,1)$ ([[Probabilità.pdf#page=27]]):
$$f_Y(y) = \frac{1}{|a|}f_X\!\left(\frac{y-b}{a}\right) = \frac{1}{\sqrt{2\pi a^2}}\,e^{-\frac{(y-b)^2}{2a^2}}$$

## Derivazioni

### Derivazione — Formula per $g$ monotona (giustifica il $|g'|$)
**Fonte:** [[Probabilità.pdf#page=27]] (formula data senza dimostrazione)
> 🧩 Derivazione mia, caso di una sola radice

$g$ crescente ($g'>0$), $x_1 = g^{-1}(y)$:
$$
\begin{aligned}
F_Y(y) &= P(g(X)\le y) = P(X \le g^{-1}(y)) = F_X(g^{-1}(y)) && g \text{ crescente conserva } \le \\
f_Y(y) &= f_X(g^{-1}(y))\cdot\frac{d g^{-1}(y)}{dy} = \frac{f_X(x_1)}{g'(x_1)} && \text{derivata della funzione inversa}
\end{aligned}
$$
$g$ decrescente ($g'<0$):
$$
\begin{aligned}
F_Y(y) &= P(X \ge g^{-1}(y)) = 1 - F_X(g^{-1}(y)) && g \text{ decrescente inverte } \le;\ X \text{ continua} \\
f_Y(y) &= -\frac{f_X(x_1)}{g'(x_1)} = \frac{f_X(x_1)}{|g'(x_1)|} && g'<0
\end{aligned}
$$
I due casi si riassumono con $|g'|$. Con più radici, $\{Y\in(y,y+dy)\}$ è l'unione disgiunta degli intervalli intorno a ciascuna $x_i$, e i contributi si sommano.

### Derivazione — $Y = aX+b$, $X\sim\mathcal{N}(0,1)$
**Fonte:** [[Probabilità.pdf#page=27]] (esempio svolto nelle slide, qui espanso)
$$
\begin{aligned}
g(x) &= ax+b,\quad g'(x) = a && a\neq0 \\
y = ax+b &\Rightarrow x_1 = \frac{y-b}{a} && \text{unica radice} \\
f_Y(y) &= \frac{f_X\left(\frac{y-b}{a}\right)}{|a|} && \text{formula generale} \\
&= \frac{1}{|a|}\cdot\frac{1}{\sqrt{2\pi}}e^{-\frac12\left(\frac{y-b}{a}\right)^2} && f_X(x) = \tfrac{1}{\sqrt{2\pi}}e^{-x^2/2} \\
&= \frac{1}{\sqrt{2\pi a^2}}e^{-\frac{(y-b)^2}{2a^2}} && |a|=\sqrt{a^2}
\end{aligned}
$$
**Risultato:** $Y\sim\mathcal{N}(b, |a|)$.
**Sanity check:** coerente con $E(aX+b) = aE(X)+b = b$ e $\sigma_Y = |a|\sigma_X = |a|$ ([[Probabilità.pdf#page=30]], vedi [[media-e-varianza]]).

> 🧩 Generalizzazione mia: con $X\sim\mathcal{N}(\mu,\sigma)$ lo stesso procedimento dà $Y\sim\mathcal{N}(a\mu+b, |a|\sigma)$. Il caso $a = 1/\sigma$, $b = -\mu/\sigma$ è la **standardizzazione** $Z = (X-\mu)/\sigma \sim \mathcal{N}(0,1)$, cioè il passaggio che giustifica $P(X>x) = Q((x-\mu)/\sigma)$ in [[variabile-aleatoria-gaussiana]].

## Spiegazione

> 🎯 Esame: «La trasformazione affine di una v.a. Gaussiana è essa stessa una v.a. Gaussiana» ([[Probabilità.pdf#page=27]]).

Metodo pratico:
1. risolvere $g(x)=y$ e trovare tutte le radici $x_i(y)$;
2. calcolare $|g'(x_i)|$;
3. sommare $f_X(x_i)/|g'(x_i)|$;
4. se per certi $y$ non ci sono radici, lì $f_Y(y) = 0$.

Esempio di non-monotonia (🧩 mio): per $Y = X^2$ le radici sono $\pm\sqrt y$ per $y>0$, quindi $f_Y(y) = [f_X(\sqrt y)+f_X(-\sqrt y)]/(2\sqrt y)$.

## Perché importa

I sistemi trasformano v.a.: un amplificatore di guadagno $a$ con offset $b$ è una trasformazione affine, il quadrato corrisponde al calcolo di una potenza istantanea, il [[companding]] è una trasformazione non lineare $F(x)$. Un quantizzatore $Q[\cdot]$ è una $g$ a gradini: $g'=0$ quasi ovunque, quindi la formula non si applica e l'uscita è discreta.

## Connessioni

- [[media-e-varianza]] — il teorema fondamentale della media permette di calcolare $E[g(X)]$ **senza** ricavare $f_Y$.
- [[variabile-aleatoria-gaussiana]] — la chiusura rispetto alle trasformazioni affini.
- [[companding]] — la legge di compressione $F(x)$ è una funzione di v.a.

## Fonti

- [[elementi-teoria-probabilita]]
- [[Probabilità.pdf#page=27]]

_Aggiornato: 2026-09-23 — creazione da ingest Probabilità.pdf_
