import urllib.parse as up
import psycopg2
from get_cep import get_cep

def select_cep(cep):
  cep = filter_cep(cep)
  try:
    up.uses_netloc.append("postgres")
    url = up.urlparse("DATABASE_URL")
    con = psycopg2.connect(database=url.path[1:],
    user = url.username,
    password = url.password,
    host = url.hostname,
    port = url.port)
  except psycopg2.Error as err:
      print(err)
      return False
  else:
    result = get_address(cep, con)
    if result:
      con.close()
      return result
    else:
      result = get_cep(cep)
      if result:
        set_address(result, con, cep)
        result = get_address(cep, con)
        con.close()
        return result
      else:
        con.close()
        return False

def filter_cep(cep):
  return cep.replace('-','')

def get_address(cep, conn):
  try:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM ADDRESSES WHERE CEP = %s;",(cep,))
    result = cursor.fetchone()
    conn.commit()
    cursor.close()
  except psycopg2.Error as err:
    print(err)
    return False
  else:
    return result

def set_address(data, conn, cep):
  try:
    cursor = conn.cursor()
    cursor.execute("INSERT INTO ADDRESSES(CEP, RUA, BAIRRO, CIDADE, UF) VALUES (%s, %s, %s, %s, %s)",(cep, data['logradouro'], data['bairro'], data['localidade'], data['uf']))
    conn.commit()
    cursor.close()
  except psycopg2.Error as err:
    print(err)
    return False
  return True
