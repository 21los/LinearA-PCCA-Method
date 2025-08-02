# 🔍 Positional-Contextual Code Analysis (PCCA) for Linear A  
> **A Paradigm Shift in Minoan Epigraphy**  
> *"85% of Linear A inscriptions aren't language - they're Bronze Age barcodes"*

[![Open in GitHub Codespaces](https://img.shields.io/badge/Open_in_Codespaces-181717?logo=github)](https://codespaces.new/your-username/LinearA-PCCA-Method)

## 🚀 Quick Start
```python
from pcca import LinearADecoder

# Load sample data
dataset = [
    {"id": "Zakros-1", "signs": ["𐝫", "𐘰", "𐄉"], "carrier": "amphora", "context": "port warehouse"},
    {"id": "Malia-3", "signs": ["𐘗", "𐘍", "𐄢"], "carrier": "tablet", "context": "granary"}
]

# Analyze with PCCA
decoder = LinearADecoder()
results = decoder.analyze(dataset)

print(f"Commodity codes: {results.commodities}")
# Output: {'𐝫': 'wine', '𐘗': 'grain'}
