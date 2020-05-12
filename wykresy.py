from furierowiec import DATASET, Series, Label, plot_stuff

# Rys 1
plot_stuff(
    Series(DATASET.OKE_CCl4, "Delay", "15C"),
    x_label=Label.time,
    y_label=Label.amplitude,
    in_x_min=-1000,
    in_x_max=5000
)

# Rys 2
plot_stuff(
    Series(DATASET.OKE_CCl4, "Delay", "15C"),
    x_label=Label.wavenumber,
    y_label=Label.amplitude,
    in_x_min=100,
    res_x_min=0,
    res_x_max=1000,
    fourierized=True
)

# Rys 3
plot_stuff(
    Series(DATASET.Raman_CCl4, "Wavenumber", "parallel", "polaryzacja równoległa"),
    Series(DATASET.Raman_CCl4, "Wavenumber", "perpendicular", "polaryzacja prostopadła"),
    x_label=Label.wavenumber,
    y_label=Label.amplitude,
    in_x_min=0,
    in_x_max=1000,
    show_legend=True
)

# Rys 6
plot_stuff(
    Series(DATASET.OKE_chloroform, "Delay", "15C", "Chloroform w 15C"),
    Series(DATASET.OKE_CCl4, "Delay", "15C", "CCl4 w 15C"),
    x_label=Label.time,
    y_label=Label.amplitude,
    in_x_min=-1000.,
    in_x_max=5000.,
    show_legend=True
)

# Rys 7.1
plot_stuff(
    Series(DATASET.OKE_CCl4, "Delay", "15C", "CCl4 w 15C"),
    x_label=Label.time,
    y_label=Label.amplitude,
    y_scale="log",
    y_limits=(0.0001, 1.),
    show_legend=True
)
# Rys 7.2
plot_stuff(
    Series(DATASET.OKE_chloroform, "Delay", "15C", "Chloroform w 15C"),
    x_label=Label.time,
    y_label=Label.amplitude,
    y_scale="log",
    y_limits=(0.0001, 1.),
    show_legend=True
)

# Rys 8
plot_stuff(
    Series(DATASET.OKE_CCl4, "Delay", "15C", "CCl4 w 15C"),
    Series(DATASET.OKE_chloroform, "Delay", "15C", "Chloroform w 15C"),
    x_label=Label.wavenumber,
    y_label=Label.amplitude,
    in_x_min=100.,
    res_x_min=100.,
    res_x_max=1000.,
    fourierized=True,
    show_legend=True
)

# Rys 9
plot_stuff(
    Series(DATASET.Raman_chloroform, "Wavenumber", "parallel", "polaryzacja równoległa"),
    Series(DATASET.Raman_chloroform, "Wavenumber", "perpendicular", "polaryzacja prostopadła"),
    x_label=Label.wavenumber,
    y_label=Label.amplitude,
    in_x_min=0,
    in_x_max=3500,
    show_legend=True
)

# Rys 12
plot_stuff(
    Series(DATASET.Raman_chloroform, "Wavenumber", "parallel", "Chloroform - polaryzacja równoległa"),
    Series(DATASET.Raman_CCl4, "Wavenumber", "parallel", "CCl4 - polaryzacja równoległa"),
    x_label=Label.wavenumber,
    y_label=Label.amplitude,
    in_x_min=0,
    in_x_max=3500,
    show_legend=True
)

# Rys 13
plot_stuff(
    Series(DATASET.OKE_CCl4, "Delay", "-5C", "-5C"),
    Series(DATASET.OKE_CCl4, "Delay", "15C", "15C"),
    Series(DATASET.OKE_CCl4, "Delay", "35C", "35C"),
    Series(DATASET.OKE_CCl4, "Delay", "55C", "55C"),
    Series(DATASET.OKE_CCl4, "Delay", "70C", "70C"),
    x_label=Label.time,
    y_label=Label.amplitude,
    in_x_min=-100.,
    in_x_max=5000.,
    show_legend=True,
    y_limits=(-0.07, 0.11)
)

# Rys 14
plot_stuff(
    Series(DATASET.OKE_chloroform, "Delay", "-5C", "-5C"),
    Series(DATASET.OKE_chloroform, "Delay", "15C", "15C"),
    Series(DATASET.OKE_chloroform, "Delay", "35C", "35C"),
    Series(DATASET.OKE_chloroform, "Delay", "55C", "55C"),
    x_label=Label.time,
    y_label=Label.amplitude,
    show_legend=True,
    y_scale="log",
    y_limits=(0.0001, 1.)
)

# Rys 15
plot_stuff(
    Series(DATASET.OKE_CCl4, "Delay", "-5C", "-5C"),
    Series(DATASET.OKE_CCl4, "Delay", "15C", "15C"),
    Series(DATASET.OKE_CCl4, "Delay", "35C", "35C"),
    Series(DATASET.OKE_CCl4, "Delay", "55C", "55C"),
    Series(DATASET.OKE_CCl4, "Delay", "70C", "70C"),
    x_label=Label.wavenumber,
    y_label=Label.amplitude,
    in_x_min=100.,
    res_x_min=0.,
    res_x_max=1000.,
    show_legend=True,
    fourierized=True,
    normalized=True
)
