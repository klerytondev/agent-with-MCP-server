from dotenv import load_dotenv
import os

load_dotenv()

SMITHERY_API_KEY = os.getenv('SMITHERY_API_KEY')

MCP_SERVERS_CONFIG = {
    # 'yfinance': {
    #     'url': f'https://server.smithery.ai/@codecbr/yahoo-finance-mcp/mcp?api_key={SMITHERY_API_KEY}',
    #     'transport': 'streamable_http',
    # },
    'yfinance': {
        'url': 'http://localhost:8000',
        'transport': 'streamable_http',
    },
    'yfinance': {
        'command': 'python',
        'args': ['D:/Users/azambuja/projects/ia_master/CODIGOS_MODULO_10/tests/mcp_server/main.py'],
        'transport': 'stdio',
    },
}