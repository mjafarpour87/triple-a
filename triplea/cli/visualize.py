import click
from triplea.cli.main import cli
import triplea.service.graph.extract as gextract
from triplea.service.click_logger import logger
import visualization.gdatarefresh as graphdatarefresh
import http.server
import socketserver

# PORT = 8000
DIRECTORY = "visualization"


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)


@cli.command("visualize", help="Visualize Graph.")
@click.option(
    "--generate",
    "-g",
    "generate_type",
    type=click.Choice(
        [
            "store",
            "gen-all",
            "article-topic",
            "article-author-affiliation",
            "article-keyword",
            "article-reference",
            "article-cited",
            "country-authorship",
        ]
    ),
    multiple=True,
    required=True,
    help="""Generate graph and export it.
                                The type of graph construction can be different. These include:

                                store : It considers all the nodes and edges that are stored in the database

                                gen-all : It considers all possible nodes and edges

                               article-topic : It considers article and topic as nodes and edges between them

                                article-author-affiliation : It considers article, author and affiliation as nodes and edges between them

                                article-keyword : It considers article and keyword as nodes and edges between them

                                article-reference : It considers article and reference as nodes and edges between them

                                article-cited : It considers article and cited as nodes and edges between them

                                country-authorship :

                                """,
)
@click.option("--port", "-p", "port", default=8000, help="port")
def visualize(generate_type, port):
    l_nodes = []
    l_edges = []
    for g_type in generate_type:
        if g_type == "store":
            raise NotImplementedError
        elif g_type == "gen-all":
            graphdict = gextract.graph_extractor_all_entity()
            l_nodes.extend(graphdict["nodes"])
            l_edges.extend(graphdict["edges"])

        elif g_type == "article-topic":
            graphdict = gextract.graph_extractor(gextract.graph_extract_article_topic)
            l_nodes.extend(graphdict["nodes"])
            l_edges.extend(graphdict["edges"])

        elif g_type == "article-author-affiliation":
            graphdict = gextract.graph_extractor(
                gextract.graph_extract_article_author_affiliation
            )
            l_nodes.extend(graphdict["nodes"])
            l_edges.extend(graphdict["edges"])

        elif g_type == "article-keyword":
            graphdict = gextract.graph_extractor(gextract.graph_extract_article_keyword)
            l_nodes.extend(graphdict["nodes"])
            l_edges.extend(graphdict["edges"])

        elif g_type == "article-reference":
            graphdict = gextract.graph_extractor(
                gextract.graph_extract_article_reference
            )
            l_nodes.extend(graphdict["nodes"])
            l_edges.extend(graphdict["edges"])

        elif g_type == "article-cited":
            graphdict = gextract.graph_extractor(gextract.graph_extract_article_cited)
            l_nodes.extend(graphdict["nodes"])
            l_edges.extend(graphdict["edges"])

        elif g_type == "country-authorship":
            graphdict = gextract.graph_extractor(gextract.graph_extract_article_country)
            l_nodes.extend(graphdict["nodes"])
            l_edges.extend(graphdict["edges"])
        else:
            logger.ERROR(f"Invalid value for '--generate' / '-g': {generate_type}")

    # print()
    # logger.DEBUG(f'Remove duplication in Nodes & Edges. ')
    n = gextract.Emmanuel(l_nodes)
    e = gextract.Emmanuel(l_edges)
    graphdict = {"nodes": n, "edges": e}
    logger.DEBUG("Update Graph Data ...")
    graphdatarefresh.refresh_interactivegraph(graphdict)
    graphdatarefresh.refresh_alchemy(graphdict)

    with socketserver.TCPServer(("", port), Handler) as httpd:
        logger.INFO(f"serving at http://localhost:{port} ....")
        httpd.serve_forever()
