#!/bin/sh
set -e

echo $DB_NAME
echo $POSTGRES_USER
echo $POSTGRES_HOST
echo $POSTGRES_PORT

#until pg_isready -h db -U admin; do 
#  sleep 3
#done

# Aguarde até que o PostgreSQL esteja disponível
until PGPASSWORD=$POSTGRES_PASSWORD psql -h $POSTGRES_HOST -p $POSTGRES_PORT -U $POSTGRES_USER -c '\q'; do
  echo "🟡 Waiting for Postgres Database Startup ($POSTGRES_HOST:$POSTGRES_PORT) ..."
  sleep 3
done

# Verifica se as variáveis de ambiente estão definidas
if [ -z "$POSTGRES_HOST" ] || [ -z "$POSTGRES_PORT" ]; then
    echo "ERROR: POSTGRES_HOST e POSTGRES_PORT precisam ser definidos."
    exit 1
fi

echo "✅ Postgres Database Started Successfully ($POSTGRES_HOST:$POSTGRES_PORT)"

# Verifica se o banco de dados já existe, caso não, o cria
PGPASSWORD=$POSTGRES_PASSWORD psql -h $POSTGRES_HOST -p $POSTGRES_PORT -U $POSTGRES_USER -tc "SELECT 1 FROM pg_database WHERE datname = '$DB_NAME'" | grep -q 1 || \
PGPASSWORD=$POSTGRES_PASSWORD psql -h $POSTGRES_HOST -p $POSTGRES_PORT -U $POSTGRES_USER -c "CREATE DATABASE $DB_NAME"

# Coletar arquivos estáticos
python manage.py collectstatic --noinput

# Realiza a migração das autenticações para o banco de dados.
python manage.py makemigrations autenticacao --noinput
python manage.py migrate autenticacao --noinput
python manage.py migrate --noinput

# Faz a migração toda vez que o serviço entrar em excecução
python manage.py makemigrations --noinput

# Sem especificar diretamente o app "core", o Django não estava identificando todas as migrações
python manage.py makemigrations core --noinput

# Aplicar migrações do banco de dados
python manage.py migrate --noinput

# Iniciar o servidor de desenvolvimento
python manage.py runserver 0.0.0.0:8000