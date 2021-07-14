import re
import matplotlib.pyplot as plt

def get_ppl_from_log(path):
  steps = []
  ppl = []
  with open(path) as f:
    for line in f:
      if " ppl: " in line and "Step " in line:
        m_step = re.search(r"(?<=Step )\d+(?=/)", line)
        steps.append(int(m_step.group(0)))
        m_ppl = re.search(r"(?<=ppl: )\s*\S+(?=;)", line)
        ppl.append(float(m_ppl.group(0)))
  
  return steps, ppl

hubert_steps, hubert_ppl = get_ppl_from_log("8\\hubert.log")
multi_steps, multi_ppl = get_ppl_from_log("8\\multi.log")

fig, ax = plt.subplots()
ax.plot(hubert_steps, hubert_ppl, label="huBERT")
ax.plot(multi_steps, multi_ppl, label="multiBERT")
ax.set_xscale("log")
ax.set_yscale("log")
ax.legend()
plt.show()