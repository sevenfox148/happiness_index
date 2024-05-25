Datasets:
- [world happiness](https://www.kaggle.com/datasets/usamabuttar/world-happiness-report-2005-present)
- [world freedom](https://www.kaggle.com/datasets/justin2028/freedom-in-the-world-2013-2022)
- [world economic freedom](https://www.fraserinstitute.org/resource-file?nid=15523&fid=20811)

## world happiness
основний датасет дослідження

1. _Log GDP per capita_ is in terms of Purchasing Power Parity (PPP) adjusted to a constant 2017 international dollars, taken from the World Development Indicators (WDI) by the World Bank 
2. The time series for _Healthy life expectancy_ at birth is constructed based on data from the World Health Organization (WHO)
3. _Social support_ (0-1) is the national average of the binary responses (0=no, 1=yes) to the Gallup World Poll (GWP) question “If you were in trouble, do you have relatives or friends you can count on to help you whenever you need them, or not?”
4. _Freedom to make life choices_ (0-1) is the national average of binary responses to the GWP question “Are you satisfied or dissatisfied with your freedom to choose what you do with your life?”
5. _Generosity_ is the residual of regressing the national average of GWP responses to the donation question “Have you donated money to a charity in the past month?” on log GDP per capita.
6. _Perceptions of corruption_ (0-1) are the average of binary answers to two GWP questions: “Is corruption widespread throughout the government or not?” and “Is corruption widespread within businesses or not?” Where data for government corruption are missing, the perception of business corruption is used as the overall corruption perception measure.
7. _Positive affect_ is defined as the average of previous-day effects 
8. _Negative affect_ is defined as the average of previous-day effects

[explanation](https://worldhappiness.report/about/)

---

## world freedom 

**_C/T_**: Indicates whether the entry is a country (c) or territory (t)

**_Status_**: F=Free, PF=Partly Free, NF=Not Free

**_PR Rating_**: Political Rights Rating

**_CL Rating_**: Civil Liberties Rating

_**A**_: Aggregate score for the "A. Electoral Process" subcategory>
- _A1_: Was the current head of government or other chief national authority elected through free and fair elections?
- _A2_: Were the current national legislative representatives elected through free and fair elections?
- _A3_: Are the electoral laws and framework fair, and are they implemented impartially by the relevant election management bodies?

**_B_**: Aggregate score for the "B. Political Pluralism and Participation" subcategory
- _B1_: Do the people have the right to organize in different political parties or other competitive political groupings of their choice, and is the system free of undue obstacles to the rise and fall of these competing parties or groupings?
- _B2_: Is there a realistic opportunity for the opposition to increase its support or gain power through elections?
- _B3_: Are the people’s political choices free from domination by forces that are external to the political sphere, or by political forces that employ extrapolitical means?
- _B4_: Do various segments of the population (including ethnic, racial, religious, gender, LGBT+, and other relevant groups) have full political rights and electoral opportunities?

_**C**_: Aggregate score for the "C. Functioning of Government" subcategory
- _C1_: Do the freely elected head of government and national legislative representatives determine the policies of the government?
- _C2_: Are safeguards against official corruption strong and effective?
- _C3_: Does the government operate with openness and transparency?

**_PR_**: Aggregate score for the Political Rights category

_**D**_: Aggregate score for the "D. Freedom of Expression and Belief" subcategory
- _D1_: Are there free and independent media?
- _D2_: Are individuals free to practice and express their religious faith or nonbelief in public and private?
- _D3_: Is there academic freedom, and is the educational system free from extensive political indoctrination?
- _D4_: Are individuals free to express their personal views on political or other sensitive topics without fear of surveillance or retribution?

**_E_**: Aggregate score for the "E. Associational and Organizational Rights" subcategory
- _E1_: Is there freedom of assembly?
- _E2_: Is there freedom for nongovernmental organizations, particularly those that are engaged in human rights– and governance-related work?
- _E3_: Is there freedom for trade unions and similar professional or labor organizations?

**_F_**: Aggregate score for the "F. Rule of Law" subcategory
- _F1_: Is there an independent judiciary?
- _F2_: Does due process prevail in civil and criminal matters?
- _F3_: Is there protection from the illegitimate use of physical force and freedom from war and insurgencies?
- _F4_: Do laws, policies, and practices guarantee equal treatment of various segments of the population?

**_G_**: Aggregate score for te "G. Personal Autonomy and Individual Rights" subcategory
- _G1_: Do individuals enjoy freedom of movement, including the ability to change their place of residence, employment, or education?
- _G2_: Are individuals able to exercise the right to own property and establish private businesses without undue interference from state or nonstate actors?
- _G3_: Do individuals enjoy personal social freedoms, including choice of marriage partner and size of family, protection from domestic violence, and control over appearance?
- _G4_: Do individuals enjoy equality of opportunity and freedom from economic exploitation?

**_CL_**: Aggregate score for the Civil Liberties category

**_Total_**: Aggregate score for all categories

[explanation](https://freedomhouse.org/reports/freedom-world/freedom-world-research-methodology)

---

## world economic freedom
- _Area 1_: Size of Government - As government spending, taxation, and
the size of government-controlled enterprises increase, government
decision-making is substituted for individual choice and economic
freedom is reduced.
- _Area 2_: Legal System and Property Rights - Protection of persons and
their rightfully acquired property is a central element of both
economic freedom and civil society. Indeed, it is the most important
function of government.
- _Area 3_: Sound Money - Inflation erodes the value of rightfully earned
wages and savings. Sound money is thus essential to protect property
rights. When inflation is not only high but also volatile, it becomes
difficult for individuals to plan for the future and thus use
economic freedom effectively.
- _Area 4_: Freedom to Trade Internationally - Freedom to exchange—in its
broadest sense, buying, selling, making contracts, and so on—is
essential to economic freedom, which is reduced when freedom to
exchange does not include businesses and individuals in other
nations.
- _Area 5_: Regulation - Governments not only use a number of tools to
limit the right to exchange internationally, they may also develop
onerous regulations that limit the right to exchange, gain credit,
hire or work for whom you wish, or freely operate your business.

[explanation](https://www.heritage.org/index/pages/report#indexHumanFlourishing)