import pytest
import os

try:
    import cartopy
    has_cartopy = True
except ImportError:
    has_cartopy = False

import matplotlib.pyplot as plt

from contextlib import contextmanager

from pyam_analysis import IamDataFrame, plotting, run_control, reset_rc_defaults

from testing_utils import plot_df, IMAGE_BASELINE_DIR, TEST_DATA_DIR


@contextmanager
def update_run_control(update):
    run_control().update(update)
    yield
    reset_rc_defaults()


@pytest.mark.mpl_image_compare(style='ggplot', baseline_dir=IMAGE_BASELINE_DIR)
def test_line_plot(plot_df):
    fig, ax = plt.subplots(figsize=(8, 8))
    plot_df.line_plot(ax=ax, legend=True)
    return fig


@pytest.mark.mpl_image_compare(style='ggplot', baseline_dir=IMAGE_BASELINE_DIR)
def test_line_no_legend(plot_df):
    fig, ax = plt.subplots(figsize=(8, 8))
    plot_df.line_plot(ax=ax, legend=False)
    return fig


@pytest.mark.mpl_image_compare(style='ggplot', baseline_dir=IMAGE_BASELINE_DIR)
def test_line_color(plot_df):
    fig, ax = plt.subplots(figsize=(8, 8))
    plot_df.line_plot(ax=ax, color='model', legend=True)
    return fig


@pytest.mark.mpl_image_compare(style='ggplot', baseline_dir=IMAGE_BASELINE_DIR)
def test_line_marker_legend(plot_df):
    fig, ax = plt.subplots(figsize=(8, 8))
    plot_df.line_plot(ax=ax, marker='model', legend=True)
    return fig


@pytest.mark.mpl_image_compare(style='ggplot', baseline_dir=IMAGE_BASELINE_DIR)
def test_line_linestyle_legend(plot_df):
    fig, ax = plt.subplots(figsize=(8, 8))
    plot_df.line_plot(ax=ax, linestyle='model', legend=True)
    return fig


@pytest.mark.mpl_image_compare(style='ggplot', baseline_dir=IMAGE_BASELINE_DIR)
def test_line_single_color(plot_df):
    fig, ax = plt.subplots(figsize=(8, 8))
    plot_df.line_plot(ax=ax, color='b', linestyle='model', legend=True)
    return fig


@pytest.mark.mpl_image_compare(style='ggplot', baseline_dir=IMAGE_BASELINE_DIR)
def test_line_filter_title(plot_df):
    fig, ax = plt.subplots(figsize=(8, 8))
    plot_df.filter({'variable': 'Primary Energy|Coal'}).line_plot(
        ax=ax, color='model', marker='scenario', legend=True)
    return fig


@pytest.mark.mpl_image_compare(style='ggplot', baseline_dir=IMAGE_BASELINE_DIR)
def test_line_update_rc(plot_df):
    with update_run_control({'color': {'model': {'test_model1': 'cyan'}}}):
        fig, ax = plt.subplots(figsize=(8, 8))
        plot_df.line_plot(ax=ax, color='model', legend=True)
    return fig


@pytest.mark.skipif(not has_cartopy, reason="requires cartopy")
@pytest.mark.mpl_image_compare(style='ggplot', baseline_dir=IMAGE_BASELINE_DIR)
def test_region():
    df = IamDataFrame(os.path.join(TEST_DATA_DIR, 'plot_iso_data.csv'))
    fig, ax = plt.subplots(
        subplot_kw={'projection': cartopy.crs.PlateCarree()}, figsize=(10, 7))
    (df
        .region_plot(
            ax=ax,
            cbar=False,
        )
     )
    return fig


@pytest.mark.skipif(not has_cartopy, reason="requires cartopy")
@pytest.mark.mpl_image_compare(style='ggplot', baseline_dir=IMAGE_BASELINE_DIR)
def test_region_cbar():
    df = IamDataFrame(os.path.join(TEST_DATA_DIR, 'plot_iso_data.csv'))
    fig, ax = plt.subplots(
        subplot_kw={'projection': cartopy.crs.PlateCarree()}, figsize=(10, 7))
    (df
        .region_plot(
            ax=ax,
            cbar=True,
        )
     )
    return fig


@pytest.mark.skipif(not has_cartopy, reason="requires cartopy")
@pytest.mark.mpl_image_compare(style='ggplot', baseline_dir=IMAGE_BASELINE_DIR)
def test_region_cbar_args():
    df = IamDataFrame(os.path.join(TEST_DATA_DIR, 'plot_iso_data.csv'))
    fig, ax = plt.subplots(
        subplot_kw={'projection': cartopy.crs.PlateCarree()}, figsize=(10, 7))
    (df
        .region_plot(
            ax=ax,
            cbar={'extend': 'both'},
        )
     )
    return fig


@pytest.mark.skipif(not has_cartopy, reason="requires cartopy")
@pytest.mark.mpl_image_compare(style='ggplot', baseline_dir=IMAGE_BASELINE_DIR)
def test_region_vmin_vmax():
    df = IamDataFrame(os.path.join(TEST_DATA_DIR, 'plot_iso_data.csv'))
    fig, ax = plt.subplots(
        subplot_kw={'projection': cartopy.crs.PlateCarree()}, figsize=(10, 7))
    (df
        .region_plot(
            ax=ax,
            vmin=0.2,
            vmax=0.4,
            cbar=False,
        )
     )
    return fig


@pytest.mark.skipif(not has_cartopy, reason="requires cartopy")
@pytest.mark.mpl_image_compare(style='ggplot', baseline_dir=IMAGE_BASELINE_DIR)
def test_region_cmap():
    df = IamDataFrame(os.path.join(TEST_DATA_DIR, 'plot_iso_data.csv'))
    fig, ax = plt.subplots(
        subplot_kw={'projection': cartopy.crs.PlateCarree()}, figsize=(10, 7))
    (df
        .region_plot(
            ax=ax,
            cmap='magma_r',
            cbar=False,
        )
     )
    return fig


@pytest.mark.skipif(not has_cartopy, reason="requires cartopy")
@pytest.mark.mpl_image_compare(style='ggplot', baseline_dir=IMAGE_BASELINE_DIR)
def test_region_crs():
    df = IamDataFrame(os.path.join(TEST_DATA_DIR, 'plot_iso_data.csv'))
    crs = cartopy.crs.Robinson()
    fig, ax = plt.subplots(subplot_kw={'projection': crs}, figsize=(10, 7))
    (df
        .region_plot(
            ax=ax,
            crs=crs,
            cbar=False,
        )
     )
    return fig


@pytest.mark.skipif(not has_cartopy, reason="requires cartopy")
@pytest.mark.mpl_image_compare(style='ggplot', baseline_dir=IMAGE_BASELINE_DIR)
def test_region_map_regions():
    df = IamDataFrame(os.path.join(TEST_DATA_DIR, 'plot_region_data.csv'))
    fig, ax = plt.subplots(
        subplot_kw={'projection': cartopy.crs.PlateCarree()}, figsize=(10, 7))
    (df
        .map_regions('iso')
        .region_plot(
            ax=ax,
            cbar=False,
        )
     )
    return fig


@pytest.mark.skipif(not has_cartopy, reason="requires cartopy")
@pytest.mark.mpl_image_compare(style='ggplot', baseline_dir=IMAGE_BASELINE_DIR,
                               savefig_kwargs={'bbox_inches': 'tight'})
def test_region_map_regions_legend():
    df = IamDataFrame(os.path.join(TEST_DATA_DIR, 'plot_region_data.csv'))
    fig, ax = plt.subplots(
        subplot_kw={'projection': cartopy.crs.PlateCarree()}, figsize=(10, 7))
    (df
        .map_regions('iso')
        .region_plot(
            ax=ax,
            legend=True,
            cbar=False,
        )
     )
    return fig


def test_bar_plot_raises(plot_df):
    pytest.raises(ValueError, plot_df.bar_plot)


@pytest.mark.mpl_image_compare(style='ggplot', baseline_dir=IMAGE_BASELINE_DIR,
                               savefig_kwargs={'bbox_inches': 'tight'})
def test_bar_plot(plot_df):
    fig, ax = plt.subplots(figsize=(8, 8))
    (plot_df
     .filter({'variable': 'Primary Energy', 'model': 'test_model'})
     .bar_plot(ax=ax, bars='scenario')
     )
    return fig


@pytest.mark.mpl_image_compare(style='ggplot', baseline_dir=IMAGE_BASELINE_DIR,
                               savefig_kwargs={'bbox_inches': 'tight'})
def test_bar_plot_h(plot_df):
    fig, ax = plt.subplots(figsize=(8, 8))
    (plot_df
     .filter({'variable': 'Primary Energy', 'model': 'test_model'})
     .bar_plot(ax=ax, bars='scenario',
               orient='h')
     )
    return fig


@pytest.mark.mpl_image_compare(style='ggplot', baseline_dir=IMAGE_BASELINE_DIR,
                               savefig_kwargs={'bbox_inches': 'tight'})
def test_bar_plot_stacked(plot_df):
    fig, ax = plt.subplots(figsize=(8, 8))
    (plot_df
     .filter({'variable': 'Primary Energy', 'model': 'test_model'})
     .bar_plot(ax=ax, bars='scenario',
               stacked=True)
     )
    return fig


@pytest.mark.mpl_image_compare(style='ggplot', baseline_dir=IMAGE_BASELINE_DIR,
                               savefig_kwargs={'bbox_inches': 'tight'})
def test_bar_plot_title(plot_df):
    fig, ax = plt.subplots(figsize=(8, 8))
    (plot_df
     .filter({'variable': 'Primary Energy', 'model': 'test_model'})
     .bar_plot(ax=ax, bars='scenario',
               title='foo')
     )
    return fig


@pytest.mark.mpl_image_compare(style='ggplot', baseline_dir=IMAGE_BASELINE_DIR,
                               savefig_kwargs={'bbox_inches': 'tight'})
def test_bar_plot_rc(plot_df):
    with update_run_control({'color': {'scenario': {'test_scenario': 'black'}}}):
        fig, ax = plt.subplots(figsize=(8, 8))
        (plot_df
         .filter({'variable': 'Primary Energy', 'model': 'test_model'})
         .bar_plot(ax=ax, bars='scenario')
         )
    return fig


@pytest.mark.mpl_image_compare(style='ggplot', baseline_dir=IMAGE_BASELINE_DIR,
                               savefig_kwargs={'bbox_inches': 'tight'})
def test_pie_plot_labels(plot_df):
    fig, ax = plt.subplots(figsize=(8, 8))
    (plot_df
     .filter({'variable': 'Primary Energy', 'model': 'test_model', 'year': 2010})
     .pie_plot(ax=ax, category='scenario')
     )
    return fig


@pytest.mark.mpl_image_compare(style='ggplot', baseline_dir=IMAGE_BASELINE_DIR,
                               savefig_kwargs={'bbox_inches': 'tight'})
def test_pie_plot_legend(plot_df):
    fig, ax = plt.subplots(figsize=(8, 8))
    (plot_df
     .filter({'variable': 'Primary Energy', 'model': 'test_model', 'year': 2010})
     .pie_plot(ax=ax, category='scenario', labels=None, legend=True)
     )
    return fig


@pytest.mark.mpl_image_compare(style='ggplot', baseline_dir=IMAGE_BASELINE_DIR,
                               savefig_kwargs={'bbox_inches': 'tight'})
def test_pie_plot_other(plot_df):
    fig, ax = plt.subplots(figsize=(8, 8))
    with update_run_control({'color': {'scenario': {'test_scenario': 'black'}}}):
        (plot_df
         .filter({'variable': 'Primary Energy', 'model': 'test_model', 'year': 2010})
         .pie_plot(ax=ax, category='scenario', cmap='viridis', title='foo')
         )
    return fig


@pytest.mark.mpl_image_compare(style='ggplot', baseline_dir=IMAGE_BASELINE_DIR,
                               savefig_kwargs={'bbox_inches': 'tight'})
def test_stack_plot(plot_df):
    fig, ax = plt.subplots(figsize=(8, 8))
    (plot_df
     .filter({'variable': 'Primary Energy', 'model': 'test_model'})
     .stack_plot(ax=ax, stack='scenario')
     )
    return fig


@pytest.mark.mpl_image_compare(style='ggplot', baseline_dir=IMAGE_BASELINE_DIR,
                               savefig_kwargs={'bbox_inches': 'tight'})
def test_stack_plot_other(plot_df):
    fig, ax = plt.subplots(figsize=(8, 8))
    with update_run_control({'color': {'scenario': {'test_scenario': 'black'}}}):
        (plot_df
         .filter({'variable': 'Primary Energy', 'model': 'test_model'})
         .stack_plot(ax=ax, stack='scenario', cmap='viridis', title='foo')
         )
    return fig
