from functools import wraps
from flask import session, redirect, url_for, g, flash
from models import Tenant, User

def check_user_authentication():
    """
    Funzione per verificare se l'utente è autenticato e associato a un tenant valido.
    Ritorna il nome completo dell'utente se autenticato, altrimenti effettua il reindirizzamento al login.
    """
    tenant_name = session.get('tenant_name')
    user_id = session.get('user_id')

    # Controllo della validità della sessione
    if not tenant_name or not user_id:
        flash("Sessione non valida o scaduta. Effettua nuovamente l'accesso.", "warning")
        return redirect(url_for('pages.login_page', tenant_name=tenant_name or ''))

    # Recupero del tenant e dell'utente dal database
    tenant = Tenant.query.filter_by(name=tenant_name).first()
    user = User.query.get(user_id)

    # Verifica che il tenant e l'utente esistano
    if not tenant or not user:
        session.clear()
        flash("Tenant o utente non trovato. Rieffettua il login.", "danger")
        return redirect(url_for('pages.login_page', tenant_name=tenant_name or ''))

    # Imposta le variabili globali per il contesto dell'applicazione
    g.tenant = tenant
    g.user = user

    # Logga le informazioni utili per il debug (opzionale)
    print(f"[DEBUG] Accesso confermato per l'utente: {user.username} nel tenant: {tenant.name}")

    # Ritorna il nome dell'utente per l'utilizzo nei template
    return f"{user.nome} {user.cognome}"