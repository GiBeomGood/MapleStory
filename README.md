# MapleStory probabilistic and statistical analysis


## 각종 정리
+ 각종 유용한 정리 모음
+ 심볼 날짜 계산기의 경우, 주간 퀘스트를 월요일에 하는 것을 가정하고 계산
+ `돌 깎기.ipynb`
  + HEXA 폴더의 파일과 내용 겹침


## 스타포스
+ 모든 분석은 스타포스의 각 시행이 independent함을 가정함
+ 즉, 선행 조건에 영향을 받지 않음을 가정
+ `스타포스 기대 비용 분석.ipynb`
  + 특정 스타포스에서 특정 스타포스(e.g., 15 -> 22)를 달성할 때, 필요한 비용의 기대값 계산
  + 0 &rightarrow; 1, $\cdots$, 24 &rightarrow; 25 강화의 기대값을 수열로 정의, 그 점화식을 구함
  + 파괴되지 않았을 때의 조건부 기대값 계산

+ `스타포스 파괴 천장 효과 예측.ipynb`
  + 스타포스 파괴 횟수에 천장 시스템을 도입했을 때, 파괴 횟수의 감소 비율 계산
  + 확률 차트를 (파괴가 잘되도록) 조정하여, 천장 시스템이 도입되어도 파괴 횟수의 기대값은 유지되게 할 수 있음
    + 천장이라는 시스템을 통해 유저들의 불쾌한 경험을 개선 가능
    + 파괴 횟수의 기대값이 유지되므로 피스(작이 전혀 안 된 아이템)의 가치 보존 가능
      + 파괴 천장 도입으로 인해 직작 수요 증가 &rightarrow; 강화 시도 증가 &rightarrow; 파괴 횟수의 기대값이 유지되더라도 피스 수요 증가 가능성 존재

+ `스타포스 파괴 확률 분석.ipynb`
  + 스타포스 과정에서 파괴되는 횟수 + 1(i.e., 해당 과정에서 필요한 피스의 개수)가 geometric distrbution을 따름의 증명 포함
  + 파괴 횟수의 pmf와 cmf(정확히는 $P(X \leq x)$가 아니라 $P(X > x)$를 다룸) 시각화

+ `스타포스 횟수 분석.ipynb`
  + 스타포스 과정에서 요구되는 시도 횟수의 기대값 계산
  + 정확하게는 스타포스 한 단계를 업그레이드할 때, 어떤 단계에서 몇 번의 시도가 발생하는지를 계산
    + e.g., 스타포스 17 &rightarrow; 18 강화를 시도할 때, 12 &rightarrow; 13 시도가 발생(파괴가 발생한다면 12단계에서 시작해야 하기 때문)하고, $\cdots$, 17 &rightarrow; 18 시도도 발생
  + 스타포스 한 단계를 업그레이드할 때, 어떤 단계에서 몇 번의 파괴가 발생하는지를 계산

  + 많은 유저들이 15 &rightarrow; 16, 16 &rightarrow; 17 단계에서 확률에 비해 너무 많은 파괴가 발생한다고 주장함
    + 하지만 실제로 분석해 봤을 때, 원래 (목표 강화 단계가 높을수록) 15 &rightarrow; 16, 16 &rightarrow; 17 단계에서 시도 횟수가 많음
    + 시도 횟수가 많으므로, 파괴 확률이 낮더라도 해당 단계에서 파괴당할 확률이 높음
    + (파일 참조) 5, 10, 15성에서 1단계 확정 상승 이벤트 날에, 스타캐치를 항상 성공하는 유저가, 파괴 방지를 하지 않으면, 15 &rightarrow; 22 시도에서 발생하는 파괴 중 57.2%를 16성에서 경험하게 됨
      + "파괴 확률은 2.1%밖에 안 되는데 왜 16성에서 이렇게 많이 터지냐"와 같은 주장은 수학적으로 완벽히 반박이 가능함
  + 번외로, 현재 스타포스는 굉장히 많은 클릭 횟수를 요구함(...)

+ `generate_prob_chart.py`
  + 스타포스 강화 단계별 확률 차트 생성 함수와 특정 스타포스를 "파괴 없이" 달성할 확률 차트 생성 함수 포함


## 추가옵션 시뮬레이터
+ 특정 수준 이상의 추가옵션을 강환불, 혹은 영환불로 뽑을 확률을 분석한 것
+ `.exe` 파일 존재


## 큐브 시뮬레이터
+ `등급업 기대값.ipynb`
  + 등급업을 위해 필요한 블랙 큐브와 레드 큐브의 기대값 계산
  + 정상화 이전의 리부트 월드를 기준으로 계산되었음
    + 가격은 수정이 필요하나, 필요한 블랙 큐브 개수는 필요한 재설정 횟수와 동일

+ `옵션 확률 계산.ipynb`
  + 큐브를 통해 목표 옵션과 대등하거나 그 이상인 옵션을 뽑을 확률 계산
    + e.g., STR +27% 옵션을 뽑는다면, STR +30%, STR +33%, STR +36% 등의 옵션을 뽑는 경우도 함께 고려


## developers
+ `크뎀 확률.ipynb`
  + 장갑 잠재옵션 재설정을 통해 크뎀을 뽑을 확률 계산
  + 크뎀 1줄을 뽑았을 때, 그것이 2줄일 확률 계산 (2.033%)

+ `history_reader.ipynb`
  + API를 통해 얻은 필자의 큐브 히스토리를 통해, 크리티컬 데미지 등장 확률이 실제 확률과 비슷한지 검증


## HEXA
+ `hexa_stat.ipynb`
  + 헥사 스탯 레벨의 pmf 및 cmf(정확하게는 $P(X \leq x)$이 아니라 $P(X > x)$를 다룸) 계산 파일