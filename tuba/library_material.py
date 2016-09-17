# -*- coding: utf-8 -*-

#Define Temperature-depended Material Properties (T1, Prop(T1), T2, Prop(T2),.....)
E_SS316=("""(
               -28.9,  197.7e3, 
                37.8,  193.95e3,
                93.33, 189.6e3,
                148.9, 186.16e3,
                204.4, 182.0e3,
                260,   178.6e3,
                315.6, 174.4e3,
                398.9, 168577,
                482.2, 162027,
                565.6, 154443,
                648.9, 146169)""")
##NU_SS316
A_SS316=("""( 
                -28.9,   14.90e-6,
                 37.8,   15.46e-6,
                 93.33,  16.02e-6,
                 148.9,  16.56e-6,
                 204.4,  17.19e-6,
                 260,    17.46e-6,
                 315.6,  17.82e-6,
                 343.3,  17.91e-6,
                 371.1,  18.00e-6,
                 398.9,  18.09e-6,
                 426.7,  18.18e-6,
                 454.4,  18.27e-6,
                 621.1,  18.90e-6,
                 648.9,  19.08e-6)""")
SH_SS316=("""( 
           -28.9, 137.9,
           37.78, 137.9,
           148.9, 107.6,
           260.0,  91.7,
           343.3,  84.81,
           426.7,  81.36,
           510.0,  78.6,
           648.9,  51.02)""")
NU_SS316=(  20.0,   0.3)

E_SS304=("""(
               -28.9,  197.7e3,
                37.8,  193.95e3,
                93.33, 189.6e3,
                148.9, 186.16e3,
                204.4, 182.0e3,
                260.0, 178.6e3,
                315.6, 174.4e3,
                398.9, 168577,
                482.2, 162027,
                565.6, 154443,
                648.9, 146169)""")
A_SS304=("""(-28.9,  14.90e-6,
                37.8,  15.46e-6,
                93.33, 16.02e-6,
                148.9, 16.56e-6,
                204.4, 17.19e-6,
                260.0, 17.46e-6,
                315.6, 17.82e-6,
                343.3, 17.91e-6,
                371.1, 18e-6,
                398.9, 18.09e-6,
                426.7, 18.18e-6,
                454.4, 18.27e-6,
                621.1, 18.9e-6,
                648.9, 19.08e-6)""")
SH_SS304=("""(  -28.9,   124.1,
                  37.78, 124.1,
                  148.9, 93.08,
                  260,   79.98,
                  343.3, 74.46,
                  426.7, 69.64,
                  510,   65.5,
                  648.9, 37.92)""")
NU_SS304=("""(20,0.3)""")

E_CSA53=("""(-28.9,  205.9e3,
              37.8,  202.01e3,
              93.33, 198.57e3,
              148.9, 195.12e3,
              204.4, 188.92e3,
              260,   188.23e3,
              315.6, 182.71e3,
              398.9, 171335,
              426.7, 166853)""")
A_CSA53=("""(-28.9,  11.25e-6,
              148.9, 12.42e-6,
              315.6, 13.32e-6,
              371.1, 13.68e-6,
              426.7, 14.04e-6)""")
SH_CSA53=("""(-28.9, 94.46,
              37.78, 94.46,
              148.9, 94.46,
              260,   94.46,
              343.3, 94.46,
              426.7, 62.05)""")
NU_CSA53=(20,0.3)

##E_SS321=(-28.9,205.9e3,37.8,202.01e3,93.33,198.57e3,148.9,195.12e3,204.4,188.92e3,260,188.23e3,315.6,182.71e3,398.9,171335,426.7,166853)
##A_SS321=(-28.9,11.25e-6,148.9,12.42e-6,315.6,13.32e-6,371.1,13.68e-6,426.7,14.04e-6)
##SH_SS321=(-28.9,94.46,37.78,94.46,148.9,94.46,260,94.46,343.3,94.46,426.7,62.05)
##NU_SS321=(20,0.3)

##L_
#-------------------------------------------------------------------------------
#               E (MPa)         nu             rho [ton/mm³]   alpha        lamb    rhoCp        allowable Stress(Sh)
dict_mat={  
"ACIER":	 [       210e3,      0.3,          7.8e-9,             10.0,        50.0,    4.0  ,      200      	 ], #Valeurs simplifiées
"RIGIDE":	 [       20000e3,    0.3,          0.0e-9,             10.9,        54.6,    3.71 ,      200 	      ],
"IMS":	 [       206e3,      0.29,         7.8e-9,              0.9,        54.6,    3.71 ,      200          ],
"A42":	 [       204e3,      0.4,          7.8e-9,              0.9,        54.6,    3.71 ,      200          ],
"Ax1":      [       165.8e3,    0.3,          13.404e-9,         12.88,        54.6,    3.71 ,      200          ],
}

#               E (MPa)         nu             rho [ton/mm³]   alpha        lamb    rhoCp        allowable Stress(Sh)
dict_mat_F={
'SS316':    [   E_SS316,        NU_SS316,      8.027e-9,        A_SS316,    50,      4 ,         SH_SS316      ],
"SS304":    [   E_SS304,        NU_SS304,      8.027e-9,        A_SS304,    50,      4 ,         SH_SS304      ],    #A358 304 CL2 (CAEPIPE) 
"CSA53":    [   E_CSA53,        NU_CSA53,      8.027e-9,        A_CSA53,    50,      4 ,         SH_CSA53      ]    #A53 Grade A Carbon Steel (CAEPIPE)

}