# Exact bounded-uniform-randomness ratio

For a fixed target u≥1, the algorithm stops at the first bid ≥u, paying all bids through that one. Uniformly choose one of k schedules. Then the optimal worst-target expected cost divided by u is (1+1/k)^(k+1). A single fair bit is the case k=2, ratio 27/8.

**Lower bound.** Assume a finite ratio R, otherwise there is nothing to prove. Each schedule must be unbounded. Because each is increasing and unbounded, their merged and sorted multiset b_1,b_2,… is locally finite; ties may be ordered arbitrarily. Put S_j=Σ_{i≤j}b_i. Just above b_j≥1 all prefix bids through position j are paid and the next qualifying bid from each schedule is a distinct entry later than j. The sum of these k entries is at least the sum of the first k tail entries (the assertion still holds if some equal bids remain immediately after position j). Hence S_{j+k}≤kR b_j by letting u decrease to b_j.

Put r_j=S_j/S_{j−1}>1 for j≥2. The last inequality gives
```
r_(j+1)⋯r_(j+k) ≤ kR(1−1/r_j).
```
Also S_{j+k}≤kR S_j gives r_i≤kR for all sufficiently large i. Sum logs from j=J to M for sufficiently large J. The sum of the logs of the products differs from k times the sum of log r_j on that range by at most a constant depending only on k,R (shift endpoints). Thus
```
Σ_(j=J)^M log[r_j^(k+1)/(r_j−1)]
      ≤ (M−J+1)log(kR)+O_(k,R)(1).
```
The minimum of r^(k+1)/(r−1) on r>1 is attained at r=(k+1)/k, as the logarithmic derivative has the sign of kr−(k+1). Divide by the number of terms and send M to infinity: kR≥k(1+1/k)^(k+1).

**Upper bound.** Let a=1+1/k. Schedule i in {0,…,k−1} bids a^i,a^(i+k),a^(i+2k),…. For a^j<u≤a^(j+1), the union of bids charged across all seeds is exactly the prefix a^0,…,a^(j+k), since each residue class occurs once among the k bids after a^j. Its sum is less than a^(j+k+1)/(a−1). Dividing by ku gives ratio at most a^(k+1)/(k(a−1))=a^(k+1). At u=1 the charged prefix ends at exponent k−1 and the same bound holds. The upper bound therefore matches.

Equal seed probabilities are essential to this statement. In particular k=2^b gives the optimum for b independent fair bits, not a claim about arbitrary probabilities over k seeds. Source: [Angelopoulos–Simon, NeurIPS 2025, §6](https://proceedings.neurips.cc/paper_files/paper/2025/file/618f396e2df006be25412505a793879a-Paper-Conference.pdf), pinned Q459. No publication priority claimed.
