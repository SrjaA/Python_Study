import requests
from bs4 import BeautifulSoup
import csv

HOST = 'https://bamper.by/'
URL = 'https://bamper.by/zchbu/zapchast_avtonomnyy-otopitel/'
HEADERS = {
    'accept'='text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'user-agent'='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
}
