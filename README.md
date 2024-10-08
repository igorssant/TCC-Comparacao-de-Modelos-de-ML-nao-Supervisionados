# TCC-Comparacao-de-Modelos-de-ML-nao-Supervisionados
T.C.C. com o tema: Comparacao de Modelos de Aprendizado de máquina não Supervisionados

## Pacientes do dataset ureia (7 dias) que contém valores nulos
10344732, 10463546, 10477920, 10553635, 10583686, 10615339, 10996857,
11542534, 11611745, 11638303, 11663336, 11833476, 12344021, 12374214,
12606435, 12934260, 13679248, 13681485, 13824877, 13827765, 13911200,
14363068, 14383658, 14623418, 14691603, 14696918, 14785854, 14816630,
15090519, 15158294, 15204620, 15409850, 15455733, 15583807, 15640315,
15763754, 15993533, 16327028, 16832227, 17131210, 17327554, 17484283,
17635990, 17718694, 17803326, 18135694, 18152377, 18213765, 18560897,
18638524, 18757959, 18976063, 19392949, 19571102, 19571265, 19694231

## Pacientes do dataset creatinina (7 dias) que contém valores nulos
10344732, 10463546, 10477920, 10553635, 10615339, 10996857, 11542534,
11611745, 11638303, 11663336, 11833476, 12344021, 12374214, 12606435,
12917345, 12934260, 13679248, 13681485, 13824877, 13827765, 13911200,
14363068, 14383658, 14623418, 14691603, 14696918, 14785854, 14816630,
15090519, 15158294, 15204620, 15409850, 15455733, 15583807, 15640315,
15763754, 15993533, 16327028, 16832227, 17131210, 17327554, 17484283,
17635990, 17718694, 17803326, 17963938, 18135694, 18152377, 18560897,
18638524, 18757959, 19571102, 19571265, 19694231

## Pacientes que possuem leitura de creatinina, mas não possuem leitura de ureia
10344732, 10477920, 10583686, 10615339, 11542534, 11638303, 12606435,
13679248, 13827765, 13911200, 14363068, 14623418, 14696918, 14785854,
15090519, 15158294, 15204620, 15455733, 15763754, 16832227, 17131210,
18213765, 18976063, 19392949, 19571102, 19571265, 19694231

Neste caso, o número de pacientes excluídos é o somatório de todas as três seções acima.

## Pacientes do dataset ureia (15 dias) que contém valores nulos
10839217, 11730347, 13784719, 15640315, 15773840, 16816440

## Pacientes do dataset creatinina (15 dias) que contém valores nulos
10463546, 10553635, 10996857, 11611745, 11663336, 11833476, 12344021,
12374214, 12934260, 13681485, 13824877, 14383658, 14691603, 14816630,
15409850, 15583807, 15640315, 15993533, 16327028, 17327554, 17484283,
17635990, 17718694, 17803326, 18135694, 18152377, 18560897, 18638524,
18757959

## Pacientes que possuem leitura de ureia, mas não possuem leitura de creatinina
10174787, 10291098, 10719064, 10839217, 11014822, 11020519, 11052292,
11226173, 11272213, 11340773, 11441773, 11481806, 11730347, 11821055,
12116314, 12430647, 12619244, 12707214, 12728628, 12902491, 12911473,
12932366, 13502902, 13573101, 13641906, 13782556, 13784719, 14217491,
14341949, 14702642, 14756130, 14870133, 14933447, 15188471, 15193194,
15288709, 15640315, 15640564, 15773840, 15791261, 15824431, 15983067,
16132846, 16225498, 16244642, 16291864, 16481693, 16679905, 16816440,
16904378, 17076438, 17229780, 17416494, 17529653, 17662799, 17790156,
17824281, 17903930, 17918473, 18049978, 18172330, 18186302, 18399764,
18441942, 18702320, 18858799, 19036718, 19057052, 19305085, 19392949,
19582136, 19607985, 19666098, 19674376, 19831176, 19884808, 19894790,
19957285

## Explicação dos resultados gerados pelo testes de Mann-Kendall
```txt
----------------------------------------------------------------------
    VARIÁVEIS RETORNADAS    |   EXPLICAÇÃO
----------------------------------------------------------------------
            trend           |   A tendência da curva.
                            |   - Increasing : tende a crescer;
                            |   - Decreasing : tende a descrescer;
                            |   - No Trend   : não possui tendência
                            |                  ou é contínua.
----------------------------------------------------------------------
            h               |   Flag de controle:
                            |   - True se há tendencia;
                            |   - False se não há tendência.
----------------------------------------------------------------------
            p               |   valor p (p-value) do teste de
                            |   significância.
                            |   Quanto menor, melhor. O ideal é
                            |   permanecer abaixo do valor 0,05.
----------------------------------------------------------------------
            z               |   Estatística de teste padrão Z.
                            |   Valores positivos de Z indicam
                            |   tendências crescentes. Valores
                            |   negativos de Z denotam tendências
                            |   decrescentes. Geralmente é utilizado
                            |   o nível de significância de 5%.
----------------------------------------------------------------------
            Tau             |   O 'Tau' de Kendall.
                            |   É uma estatística usada para medir a
                            |   correlação de postos entre duas
                            |   quantidades medidas.
                            |   - 1 : Indica forte forte tendência
                            |   crescente;
                            |   - 0 : Indica que não há tendência;
                            |   - (-1) : Indica forte tendência
                            |   decrescente.
----------------------------------------------------------------------
            s               |   A pontuação de Mann-Kendall.
                            |   Esta variável serve de base para
                            |   determinar a tendência da reta e,
                            |   por consequência, 'trend'.
                            |   - s > 0 : tende a crescer;
                            |   - s = 0 : não possui tendência
                            |             ou é contínua;
                            |   - s < 0 : tende a decrescrescer.
----------------------------------------------------------------------
            var_s           |   A variância de S.
                            |   Esta variável quantifica a incerteza
                            |   associada à variável 's' e, por
                            |   consequência, a variável 'trend'.
                            |   Quanto mais baixa, melhor.
                            |   valores altos de 'var_s' indicam
                            |   alta incerteza, enquanto valores
                            |   baixos de 'var_s' sugerem uma
                            |   estimação de tendência com
                            |   altos níveis de confiança.
----------------------------------------------------------------------
            slope           |   A inclinação da curva.
                            |   - slope > 0 : a curva faz parte de
                            |   uma função crescente;
                            |   - slope = 0 : a curva faz parte de
                            |   uma função contínua;
                            |   - slope < 0 : a curva faz parte de
                            |   uma função decrescente.
----------------------------------------------------------------------
            intercept       |   O ponto no qual a curva toca o
                            |   eixo y.
----------------------------------------------------------------------
```
