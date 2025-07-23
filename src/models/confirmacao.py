from src.models.user import db
from datetime import datetime

class Confirmacao(db.Model):
    __tablename__ = 'confirmacoes'
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    familiares = db.Column(db.Text, nullable=True)  # Lista de familiares que não vão
    vai_comparecer = db.Column(db.Boolean, nullable=False)  # True = SIM, False = NÃO
    data_confirmacao = db.Column(db.DateTime, default=datetime.utcnow)
    ip_address = db.Column(db.String(45), nullable=True)  # Para evitar duplicatas
    
    def __repr__(self):
        return f'<Confirmacao {self.nome}: {"SIM" if self.vai_comparecer else "NÃO"}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'familiares': self.familiares,
            'vai_comparecer': self.vai_comparecer,
            'data_confirmacao': self.data_confirmacao.isoformat() if self.data_confirmacao else None,
            'ip_address': self.ip_address
        }

