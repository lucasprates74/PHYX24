import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sb
plt.rcParams.update({'font.size': 16}) # change plot font size

PATH = "knot/rog/img/"
pxl_to_cm = 22.7 / 1080


def sturge(n):
    return int(np.ceil(2 + np.log2(n)))


# n = 6  # trial number 
starting_frames = [10, 0, 350, 600, 1450, 750]
for n in range(1, 12):
    file = f'knot/rog/lp_rog_vids/trial{n}/rog.txt'
    frm, xc, yc, rog = np.loadtxt(file, delimiter=' ', unpack=True)

    rog = rog * pxl_to_cm
    
    start = -31
    
    # find mean and standard error, and round both to the first sig fig of the standard error
    mean = np.mean(rog[start:])
    err = np.std(rog[start:]) / np.sqrt(len(rog[start:]))
    first_sig_fig = -int(np.floor(np.log10(err)))
    mean, err = round(mean, first_sig_fig), round(err, first_sig_fig)
    print("Mean = ", mean, "+/-", err, "cm")
    
    plt.figure(figsize=(8,4))
    plt.suptitle(f"Trial {n} Equilibrium $R_g$: $<R_g>$ = {mean} $\\pm$ {err} cm")
    plt.subplot(1,2,1)
    plt.plot(frm, rog)
    plt.xlim(frm[start], frm[-1])
    plt.xlabel("time (frame number)")
    plt.ylabel("$R_{g}$ (cm)")
    plt.grid(alpha=0.5)
    # plt.show()


    

    bins = np.linspace(np.min(rog[start:]), np.max(rog[start:]), sturge(len(rog[start:])))

    plt.subplot(1,2,2)
    sb.distplot(rog[start:], bins, rug=True)
    plt.xlabel("$R_{g}$ (cm)")
    plt.grid(alpha=0.5)
    plt.savefig(PATH + f'trial{n}', dpi=300, bbox_inches='tight')
    plt.show()