from app import app, db
from models import Tenant, User
from werkzeug.security import generate_password_hash

with app.app_context():
    # Crea un tenant reale
    tenant_name = 'spotexsrl'
    tenant = Tenant(name=tenant_name, domain='spotexsrl.com', is_active=True)
    db.session.add(tenant)
    db.session.commit()
    print(f'Tenant creato: {tenant.name}')

    # Crea un utente reale legato al tenant appena creato
    user = User(
        username='QUAALE',
        email='alessio.quagliara@spotexsrl.com',
        password=generate_password_hash('WtQ5i8h20@', method='pbkdf2:sha256'),
        role='admin',
        is_active=True,
        nome='Alessio',
        cognome='Quagliara',
        profilo_foto='images/default_avatar.png',  # Immagine profilo predefinita
        tenant_id=tenant.id
    )
    db.session.add(user)
    db.session.commit()
    print(f'Utente creato: {user.username} ({user.nome} {user.cognome})')