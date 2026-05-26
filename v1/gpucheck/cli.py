import click

from gpucheck.checks.driver_check import DriverCheck
from gpucheck.checks.cuda_check import CudaCheck
from gpucheck.checks.runtime_check import RuntimeCheck
from gpucheck.checks.kubernetes_check import KubernetesCheck
from gpucheck.checks.vram_check import VramCheck
from gpucheck.checks.dcgm_check import DcgmCheck
from gpucheck.checks.triton_check import TritonCheck

from gpucheck.utils.formatter import print_results
from gpucheck.utils.json_formatter import format_json
from gpucheck.utils.logger import setup_logger


@click.group()
def cli():
    pass


@cli.command()
@click.option("--json-output", is_flag=True)
@click.option("--verbose", is_flag=True)
def run(json_output, verbose):

    logger = setup_logger(verbose)

    logger.info("Starting GPU cluster diagnostics")

    checks = [
        DriverCheck(),
        CudaCheck(),
        RuntimeCheck(),
        KubernetesCheck(),
        VramCheck(),
        DcgmCheck(),
        TritonCheck()
    ]

    results = []

    for check in checks:
        logger.debug(f"Running {check.__class__.__name__}")
        results.append(check.run())

    if json_output:
        print(format_json(results))
    else:
        print_results(results)