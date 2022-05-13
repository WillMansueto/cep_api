import requests
from requests.exceptions import HTTPError

def get_cep(cep):
  try:
    apiurl = f"https://viacep.com.br/ws/{cep}/json/"
    response = requests.get(apiurl)
    response.raise_for_status()
    data = response.json()
    if data:
      if "erro" in data:
        return False
      else:
        return data
    else:
      return False

  except HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')
    return False
  except Exception as err:
    print(f'Other error occurred: {err}')
    return False