from github import Github

# Autentificación (reemplaza con tu token de acceso personal)
token = "tu_token_de_acceso"
g = Github(token)

# Obtener el repositorio
repo = g.get_repo("tu_usuario/tu_repositorio")

# Crear un issue
issue = repo.create_issue(title="Nuevo issue creado automáticamente", body="Este issue ha sido creado por un script de Python.")
