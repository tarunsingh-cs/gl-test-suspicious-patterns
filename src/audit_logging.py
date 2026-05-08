def log_contract_access(user_id, contract_id, action):
    """Log all contract access events."""
    timestamp = datetime.now()
    event = {
        'user': user_id,
        'contract': contract_id,
        'action': action,
        'time': timestamp
    }
    audit_log.append(event)

def retrieve_access_logs(contract_id):
    """Get all access history for contract."""
    return audit_log.filter(contract_id=contract_id)
