import os
import matplotlib.pyplot as plt
from solar_tools.settings import MEDIA_ROOT


def display_csv_graph(monthly_averages, lat, long, year):
    plt.figure(figsize=(8, 8))

    plt.xlabel('Month', fontsize=8)
    plt.xticks(range(1, 13), fontsize=8)
    plt.ylabel('Irradiance W/m^2', fontsize=8)

    line1, = plt.plot(monthly_averages.GHI, label='GHI')
    line2, = plt.plot(monthly_averages.DHI, label='DHI')
    line3, = plt.plot(monthly_averages.DNI, label='DNI')

    line1.set_label('GHI')
    line2.set_label('DHI')
    line3.set_label('DNI')

    plt.legend(prop={'size': 6})
    plt.title(f'Average Monthly Solar Irradiance ({year})')
    plt.tight_layout()
    filename = f'{lat}_{long}_{year}_graph.png'
    relative_img_filepath = f'graph_imgs/{filename}'
    abs_img_filepath = os.path.join(MEDIA_ROOT, relative_img_filepath)
    plt.savefig(abs_img_filepath)
    return relative_img_filepath
