# Kontent

Aplicação com Django Rest Framework para montar um CRUD que gerencia conteúdos.


# Endpoints da API

| Endpoint               | Endpoint | Objetivo                    |
|------------------------|------------|-----------------------------|
| api/contents/          | POST       | Cadastrar conteúdo         |
| api/contents/          | GET        | Listar conteúdos           |
| api/contents/<content_id>/ | GET     | Filtrar conteúdo           |
| api/contents/<content_id>/ | PATCH   | Atualizar conteúdo         |
| api/contents/<content_id>/ | DELETE  | Deletar conteúdo           |
| api/contents/filter/   | GET        | Filtrar conteúdo por query param |
