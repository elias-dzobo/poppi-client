
from client import PoppiClient


client = PoppiClient()

vs = client.get_vectorstore('number-systems-001')

context = vs.retrieve([-5.51133715e-02, 4.03841548e-02, -9.48631763e-02, -1.18309803e-01, -7.94157088e-02, -2.38716770e-02, 3.93027104e-02, 5.23600541e-02, 5.14049307e-02, -3.91207896e-02, -1.64536443e-02, 7.82067254e-02, 9.35971513e-02, 1.90692581e-02, -5.56232780e-02, -8.21795762e-02, -4.51802276e-02, 1.83554571e-02, 6.00336818e-03, -3.99121456e-03, -1.33295665e-02, 3.12755890e-02, -1.07304238e-01, 3.63356210e-02, 1.46014811e-02, 1.25307571e-02, -3.14652286e-02, -2.41817068e-02, 5.49579188e-02, -9.63313878e-02, -4.59358543e-02, 9.01958942e-02, 1.33410469e-01, -1.16160298e-02, -6.88490272e-02, -1.74477287e-02, 9.01269838e-02, -2.05553770e-02, -7.15259463e-02, 1.16370052e-01, -6.78018630e-02, -4.09694426e-02, 7.91102052e-02, 4.20706868e-02, -4.47672568e-02, 5.48831113e-02, -8.97023641e-03, 6.95538893e-02, -2.47242097e-02, -1.04282433e-02, -3.78946140e-02, 6.51471168e-02, -4.62930165e-02, 5.91914840e-02, -3.87776010e-02, -6.82843104e-02, 1.20434631e-02, 4.43447791e-02, -7.70036429e-02, -9.60007403e-03, -2.76280735e-02, 4.00225334e-02, -3.03252060e-02, -8.52790847e-02, 5.25914952e-02, 6.74254373e-02, -2.10388135e-02, 2.73133162e-03, -1.79736707e-02, 1.31175630e-02, 3.24405730e-02, 3.12068406e-02, 2.88100224e-02, 5.58035858e-02, 2.29387432e-02, 4.66901027e-02, -4.21266221e-02, -4.07980978e-02, 2.41715573e-02, 1.29287476e-02, -1.73772243e-03, -5.34083620e-02, -1.19821057e-02, 3.33517753e-02, 3.93116809e-02, -3.49355228e-02, -7.92026520e-02, 5.16910031e-02, 1.77358761e-02, -1.20819852e-01, 5.34138381e-02, 1.84342163e-04, 9.27660242e-02, 4.01076339e-02, -3.44182216e-02, 2.81010438e-02, 2.55938899e-02, -4.96330112e-03, 1.10952137e-02, 1.39404029e-01, 1.14697302e-02, 3.01722642e-02, -2.13549566e-02, 2.23712586e-02, -1.84396915e-02, -3.15526151e-03, 4.97027524e-02, 6.83881119e-02, 3.94997895e-02, -7.08296970e-02, 3.33131291e-02, -8.56286809e-02, -1.49250068e-02, -1.50950132e-02, 1.56350043e-02, -1.02620721e-01, 4.08889093e-02, 3.54829542e-02, -8.16981960e-03, -5.75394705e-02, 2.40024626e-02, 8.13923404e-03, -5.38198452e-04, 3.98525745e-02, -3.12825432e-03, 7.77871758e-02, -5.62368743e-02, -4.48490107e-33, -1.00265935e-01, 4.40573953e-02, 4.31358963e-02, 6.39846623e-02, -6.47023618e-02, -4.81165275e-02, -4.82384637e-02, 4.50682419e-04, 3.30247432e-02, 8.15537795e-02, -2.20928825e-02, 5.26494868e-02, 8.33182037e-02, -3.72446887e-02, 1.29216120e-01, -6.05755113e-02, 5.24693020e-02, 9.21414141e-03, 2.74415221e-02, -4.73782495e-02, 3.70296389e-02, 4.40592468e-02, -2.24378109e-02, -3.01180370e-02, 1.60859466e-01, 8.60401243e-02, 1.84974242e-02, -7.27628246e-02, 7.67141432e-02, -7.59240659e-03, -2.40312517e-02, 6.88817129e-02, -6.00948706e-02, -4.82660672e-03, 2.30143275e-02, 1.92302652e-02, 2.72639059e-02, -1.55173168e-02, 5.96292019e-02, -7.89406225e-02, -2.34771310e-03, 3.97130623e-02, -1.91592537e-02, -3.16989012e-02, 3.22899818e-02, 4.32475880e-02, 6.37658760e-02, 4.73164134e-02, 2.86651738e-02, -3.73680703e-02, -7.02780262e-02, 2.49983128e-02, -9.93884504e-02, 6.97355438e-03, 9.21615213e-02, -1.00110233e-01, 1.30700488e-02, 8.76986235e-03, -3.70370485e-02, 5.33763207e-02, 4.74853703e-04, 3.25763896e-02, 5.26808240e-02, -5.45241609e-02, -4.67101447e-02, -2.35058758e-02, -3.09358872e-02, -7.97553137e-02, 4.90859747e-02, 9.93900821e-02, -1.32269368e-01, 3.41080665e-03, 2.69606188e-02, 6.56291544e-02, -2.26383768e-02, 2.288])

print(vs)

print(context)