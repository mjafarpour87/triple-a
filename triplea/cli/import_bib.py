import click
from triplea.service.click_logger import logger
from triplea.service.repository.state.initial import (
    get_article_from_bibliography_file_format,
)
from triplea.cli.main import cli


@cli.command("import", help="import article from .bib , .enw , .ris file format.")
@click.argument("filename", type=click.Path(exists=True))
def import_single_file(filename):
    logger.INFO("Import file type : .bib , .enw , .ris")
    r = get_article_from_bibliography_file_format(filename)
    if r:
        logger.INFO("Import complete.")
    else:
        logger.ERROR("Import incomplete.")


if __name__ == "__main__":
    import_single_file()
