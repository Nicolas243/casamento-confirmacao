from flask import Blueprint, request, jsonify
from src.models.confirmacao import db, Confirmacao

confirmacao_bp = Blueprint('confirmacao', __name__)

@confirmacao_bp.route('/confirmar', methods=['POST'])
def confirmar_presenca():
    """Endpoint para confirmar presença"""
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({'error': 'Dados não fornecidos'}), 400
        
        nome = data.get('nome', '').strip()
        vai_comparecer = data.get('vai_comparecer')
        familiares = data.get('familiares', '').strip()
        
        # Validações
        if not nome:
            return jsonify({'error': 'Nome é obrigatório'}), 400
        
        if vai_comparecer is None:
            return jsonify({'error': 'Confirmação de presença é obrigatória'}), 400
        
        # Verificar se já existe confirmação para este nome
        confirmacao_existente = Confirmacao.query.filter_by(nome=nome).first()
        if confirmacao_existente:
            return jsonify({'error': 'Já existe uma confirmação para este nome'}), 409
        
        # Criar nova confirmação
        nova_confirmacao = Confirmacao(
            nome=nome,
            vai_comparecer=bool(vai_comparecer),
            familiares=familiares if not vai_comparecer else None,
            ip_address=request.remote_addr
        )
        
        db.session.add(nova_confirmacao)
        db.session.commit()
        
        return jsonify({
            'message': 'Confirmação registrada com sucesso!',
            'confirmacao': nova_confirmacao.to_dict()
        }), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': f'Erro interno: {str(e)}'}), 500

@confirmacao_bp.route('/confirmacoes', methods=['GET'])
def listar_confirmacoes():
    """Endpoint para listar todas as confirmações"""
    try:
        confirmacoes = Confirmacao.query.order_by(Confirmacao.data_confirmacao.desc()).all()
        
        resultado = {
            'total': len(confirmacoes),
            'confirmaram_sim': len([c for c in confirmacoes if c.vai_comparecer]),
            'confirmaram_nao': len([c for c in confirmacoes if not c.vai_comparecer]),
            'confirmacoes': [c.to_dict() for c in confirmacoes]
        }
        
        return jsonify(resultado), 200
        
    except Exception as e:
        return jsonify({'error': f'Erro interno: {str(e)}'}), 500

@confirmacao_bp.route('/estatisticas', methods=['GET'])
def obter_estatisticas():
    """Endpoint para obter estatísticas das confirmações"""
    try:
        total = Confirmacao.query.count()
        confirmaram_sim = Confirmacao.query.filter_by(vai_comparecer=True).count()
        confirmaram_nao = Confirmacao.query.filter_by(vai_comparecer=False).count()
        
        return jsonify({
            'total_confirmacoes': total,
            'confirmaram_sim': confirmaram_sim,
            'confirmaram_nao': confirmaram_nao,
            'percentual_sim': round((confirmaram_sim / total * 100) if total > 0 else 0, 2),
            'percentual_nao': round((confirmaram_nao / total * 100) if total > 0 else 0, 2)
        }), 200
        
    except Exception as e:
        return jsonify({'error': f'Erro interno: {str(e)}'}), 500

