# Page Proof 2650030 — Reply to Author Queries and List of Corrections

**Article:** On the domination energy of *k*-uniform hypergraphs with applications to supply chain resilience
**MS ID:** 2650030 · IJWMIP · DOI 10.1142/S021969132650030X
**Corresponding author:** Abdulkafi Sanad
**Deadline:** 3 September 2026

---

## PART 1 — Answers to the Author Queries (AQ)

### AQ 1 (Page 1) — "Please provide valid ORCID ID of all authors."

> **Answer:** Three of the four ORCID iDs are already correct in the proof. Only the third author is
> missing. Please insert on **Page 18, line 9**, replacing the incomplete link `https://orcid.org/`:
>
> **Abdulqawe Kaed — https://orcid.org/0009-0007-4272-2158**
>
> The other three are confirmed correct as printed:
> - Abdulkafi Sanad — https://orcid.org/0009-0004-6877-9281
> - Sultan Mahde — https://orcid.org/0000-0003-2325-0240
> - Abaid Ullah — https://orcid.org/0009-0003-4880-186X

### AQ 2 (Page 3) — "Please approve the short running head."

> **Answer:** Approved. The short running head *"Domination energy of k-uniform hypergraphs"* is
> correct and may be retained as printed.

### AQ 3 (Page 15) — "Please approve the insertion of the text citation for Fig. 4."

> **Answer:** Not approved in its present position. The citation "(Fig. 4)" has been inserted at the
> end of the proof of Theorem 13, which concerns the greedy set-cover guarantee and is unrelated to
> the figure. Please **delete "(Fig. 4)" from Page 15, line 5**, and instead cite the figure — together
> with Table 1, which is currently uncited — at the start of Sec. 4.5 (Correction 4 below).

### AQ 4 (Page 17) — "Please confirm whether we can remove the sections 'Declaration of interests / Author contributions'."

> **Answer:** Confirmed. Both sections may be removed, exactly as marked in the proof
> (Page 17, lines 34–40).

---

## PART 2 — Corrections

### GROUP A — Substantive (please give these particular attention)

#### Correction 1 — Page 17, lines 26–32 — **duplicated paragraph**

The closing paragraph of the Conclusion appears **twice**, in two different wordings. Please delete
the second occurrence.

**DELETE** from "Beyond the extremal…" (line 26) through "…graphs and hypergraphs.¹³,²⁸,²⁷" (line 32):

> ~~Beyond the extremal and structural questions that remain open, a natural continuation of this work
> concerns information processing on higher-order networks. The domination matrix is a symmetric shift
> operator whose diagonal marks a one-hop covering set of vertices, and the spectral bounds obtained in
> Sec. 3 control the quantities spectral radius, trace norm, eigenvalue spread that govern filter bank
> and multiscale constructions for signals on graphs and hypergraphs.¹³,²⁸,²⁷~~

**KEEP** the final sentence and run it on directly after "…for graph and hypergraph signals.¹³,²⁸,²⁷"
(line 26), so that the paragraph ends:

> …that govern filter-bank constructions for graph and hypergraph signals.¹³,²⁸,²⁷ Investigating
> domination-based multiscale decompositions of hypergraph signals is left for future work.

#### Correction 2 — Page 16, Table 2, "Customer preference" row — **word lost in typesetting**

The entry reads "Preferred supplier status in 1". The word *RFPs* has been lost.

- **Replace:** Preferred supplier status in ~~1~~
- **With:** Preferred supplier status in **RFPs**

#### Correction 3 — Page 9 (line 8–9) and Page 10 (caption of Fig. 2) — **figure does not match its caption**

Figure 2 shows nine separate hypergraphs $H_1,\dots,H_9$, none of which is a complete hypergraph, so
both the caption and the sentence pointing to it are inaccurate. The artwork is to be **kept as
printed**; please amend the two wordings instead.

**(a) Page 9, lines 8–9 — last sentence of Definition 7:**

- **Replace:** "See Fig. 2 for an illustration of a ~~complete~~ 3-uniform hypergraph."
- **With:** "See Fig. 2 for **examples of 3-uniform hypergraphs**."

**(b) Page 10 — caption of Fig. 2:**

- **Replace:** "Fig. 2. ~~A complete 3-uniform hypergraph.~~"
- **With:** "Fig. 2. **Examples of 3-uniform hypergraphs.**"

#### Correction 4 — Page 16, Sec. 4.5, line 2 — **insert citations for Table 1 and Fig. 4**

Table 1 and Fig. 4 are not cited anywhere in the text. Please insert one sentence at the beginning of
Sec. 4.5, before "The quantitative figures reported in Tables 2 and 3…":

> **INSERT:** Table 1 summarizes the tiered mitigation framework derived from these criticality
> scores, and Fig. 4 shows the corresponding monitoring architecture: enterprise data sources feed the
> criticality analysis engine, whose outputs drive the decision-support layer.

#### Correction 5 — Page 17, lines 4–5 — **inconsistency with Theorem 13**

The Conclusion states an $O(\log n)$ guarantee, whereas Theorem 13 (Page 14) proves the sharper
constant $H_{m_2}\le\ln m_2+1$.

- **Replace:** "…(Algorithm 1) provides an ~~$O(\log n)$ approximation guarantee for identifying
  companies whose disruption would maximize cascade impact.~~"
- **With:** "…(Algorithm 1) comes with a logarithmic approximation guarantee: its greedy selection
  phase returns a covering set of companies within a factor $H_{m_2}\le\ln m_2+1$ of the minimum,
  where $m_2$ is the number of production processes."

---

### GROUP B — Language and metadata

#### Correction 6 — Page 2, lines 13–15 — missing em-dashes (sentence is ungrammatical)

- **Replace:** "Real-world systems social networks, protein interactions, supply chains often involve
  multi-way relationships"
- **With:** "Real-world systems**—**social networks, protein interactions, supply chains**—**often
  involve multi-way relationships"

#### Correction 7 — Page 3, lines 4–6 — missing em-dashes

- **Replace:** "their analytic quality frame bounds, filter localization, stability of reconstruction
  is controlled by spectral quantities"
- **With:** "their analytic quality**—**frame bounds, filter localization, stability of
  reconstruction**—**is controlled by spectral quantities"

#### Correction 8 — Page 3, lines 22–24 — missing em-dashes

- **Replace:** "whose diagonal marks a minimum dominating set in signal-processing language, a set of
  vertices from which the whole network is reachable in one hop and the domination energy is its trace
  norm."
- **With:** "whose diagonal marks a minimum dominating set**—**in signal-processing language, a set of
  vertices from which the whole network is reachable in one hop**—**and the domination energy is its
  trace norm."

#### Correction 9 — Page 17, lines 1–3 — missing em-dashes

- **Replace:** "Our criticality metrics domination energy, fragility index, cascade risk and
  resilience score offer quantitative measures"
- **With:** "Our criticality metrics**—**domination energy, fragility index, cascade risk and
  resilience score**—**offer quantitative measures"

#### Correction 10 — Page 3 (line 15) and Page 19 (Ref. [24], line 23) — missing en-dash in a name

- **Replace (both places):** "Weierstrass Mandelbrot"
- **With:** "Weierstrass**–**Mandelbrot"

#### Correction 11 — Page 1, lines 13–16 — affiliations: missing cities

- Line 14, **replace:** "Albaydha University, Yemen"
  **with:** "Albaydha University, **Radaa**, Yemen"
- Line 16, **replace:** "Thamar University, Yemen"
  **with:** "Thamar University, **Dhamar**, Yemen"

#### Correction 12 — Page 16, line 16 — hyphen (optional)

- **Replace:** "the well established concept of graph energy"
- **With:** "the well-established concept of graph energy"

#### Correction 13 — Page 17, line 24 — hyphen (optional)

- **Replace:** "a dominating set is a one hop covering set of vertices"
- **With:** "a dominating set is a one-hop covering set of vertices"

#### Correction 14 — Page 19, Ref. [26], line 29 — hyphen (optional)

- **Replace:** "wavelet transform based smooth ordering"
- **With:** "wavelet transform-based smooth ordering"

---

## PART 3 — One point to verify yourself before you send

**E-mail addresses (Page 1, lines 17–20).** The proof prints:

- `abdulkafisanad@stu.ynu.edu.cn`
- `sultan.mahde@gmail.com`
- `abdulqawe.dabouan@tu.edu.ye`
- `ullahabaid@stu.ynu.edu.cn`

Please check each against the address its owner actually uses. Two of them differ from addresses used
earlier in the project (`sutanmahde@gmail.com`, `dabouaan@tu.edu.ye` — note the doubled *a*), so
confirm the spelling with Sultan Mahde and Abdulqawe Kaed directly. A wrong e-mail in a published
paper cannot be corrected without an erratum.
