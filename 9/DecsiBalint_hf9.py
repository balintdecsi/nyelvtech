### 3.

# import spacy
import hu_core_ud_lg
nlp = hu_core_ud_lg.load()

szofaj_szotar = {'VERB':['V'],'NOUN':['N'],'PUNCT':['WPUNCT','SPUNCT'],'ADJ':['A'],'CONJ':['Con'],'SCONJ':['Con'],'PRON':['Pro']}

with open("9\\mnsz_minta.sima", encoding="utf8") as sima_f:
  with open("9\\mnsz_minta.elemzett", encoding="utf-8") as elemz_f:
    for line in sima_f:
      sima_doc = nlp(line)
      elemz_doc = elemz_f.readline().split(" ")
      elemz_doc_iter = iter(elemz_doc)
      if len(sima_doc) == len(elemz_doc):
        for token in sima_doc:
          elemz_token = next(elemz_doc_iter)
          elemz_token_parts = elemz_token.split("/")
          elemz_szofaj = elemz_token_parts[-1].split(".")[0]
          if token.pos_.lower() == elemz_szofaj.lower() or elemz_szofaj in szofaj_szotar.get(token.pos_):
            # print(f"{token.text} [{token.pos_}] <-> {elemz_token_parts[0]} [{elemz_szofaj}]\n")
            continue
          else:
            print(f"{token.text} [{token.pos_}] <-> {elemz_token_parts[0]} [{elemz_szofaj}]\n")