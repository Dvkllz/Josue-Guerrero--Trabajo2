__author__ = "Josue David Guerrero Velez"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "josue.guerrerov@campusucc.edu.co"

'''----------------------------------------------------------------
# Importaciones
----------------------------------------------------------------'''
from CuentaAhorros import CuentaAhorros
from CuentaCorriente import CuentaCorriente
from CDT import CDT
class simuladorbancario:
    #----------------------------------------------------------------
    # Atributos
    #----------------------------------------------------------------
    __cedula = ''
    __nombre = ''
    
    __cuentacorriente = CuentaCorriente()
    __cuentaahorros = CuentaAhorros ()
    __cdt = CDT()
    
    __mesActual = 0
    
    #----------------------------------------------------------------
    # Metodos
    #----------------------------------------------------------------
    
    _method_ = 'ConsignaCuentaCorriente'
    _params_ = 'monto'
    _returns_ = 'nada'
    _Description_ ='Este metodo consigna un monto a la cuenta corriente'
    def ConsignarCuentaCorriente (self, monto):
    #aqui inicia el monto
    #self.__cuentacorriente.saldo = self._cuentacorriente.saldo + monto 
    #modo no recomendado
        self.__cuentacorriente.ConsignarValor(monto)
    

    
    _method_ = 'DarSaldo'
    _params_ = 'ninguno'
    _returns_ = 'Saldo'
    _Description_ ='Este metodo retorna el saldo'
    def DarSaldo (self):
        return self.__saldo 
    
    
    
    _method_ = 'CalcularSaldoTotal'
    _params_ = 'ninguno'
    _returns_ = 'Saldo total'
    _Description_ ='Este metodo retorna el saldo total de todas las cuentas'
    def CalcularSaldoTotal (self):
        total = self._cuentacorriente.DarSaldo()+self._cuentaahorrors.DarSaldo()
        return total 
    
    

    _method_ = 'PasarAhorrosACorriente'
    _params_ = 'ninguno'
    _returns_ = 'ninguno'
    _Description_ ='Este metodo transfiere el saldo de ahorros a corriente'
    def PasarAhorrosACorriente(self):
        saldotemporal = self.__cuentaahorros.DarSaldo()
        self.__cuentaahorros.RetirarValor(saldotemporal)
        self.__cuentacorriente.ConsignarValor(saldotemporal)


        
    _method_ = 'DarSaldo'
    _params_ = 'ninguno'
    _returns_ = 'Saldo'
    _Description_ ='Este metodo retorna el saldo'
    def DarSaldo (self):
        return self.__saldo
    


    _method_ = 'ahorrar'
    _params_ = 'monto'
    _returns_ = 'nuevos ahorros'
    _Description_ ='Este metodo transfiere el saldo de corriente a ahorros'
    def ahorro (self):
        saldotemporal2 = self.__cuentacorriente.DarSaldo()
        self.__cuentacorriente.RetirarValor(saldotemporal2)
        self.__cuentaahorros.ConsignarValor(saldotemporal2)


    _method_ = 'RetirarAhorro'
    _params_ = 'monto'
    _returns_ = 'SaldoRestante'
    _Description_ = 'Este metodo nos permite retirar el dinero de nuestra cuenta de ahorros'
    def RetirarAhorro (self, monto):
        self.__cuentaahorros.RetirarValor()



    _method_ = 'RetirarTodo'
    _params_ = 'Ninguno'
    _returns_ = 'Ninguno'
    _Description_ = 'Este metodo nos permite retirar el dinero total de nuestra cuenta bancaria'
    def RetirarTodo (self):
        saldoretirado = self.__cuentacorriente.DarSaldo() + self.__cuentaahorros.DarSaldo
        self.__cuentadeahorros.RetirarValor(self.__cuentadeahorros.DarSaldo())
        self.__cuentacorriente.RetirarValor(self.__cuentacorriente.DarSaldo())
        return 'Usted acaba de teritrar '+saldoretirado


    _method_ = 'DuplicarAhorro'
    _params_ = 'Ninguno'
    _returns_ = 'ninguno'
    _Description_ = 'Este metodo nos permite duplicar los ahorros'
    def DuplicarAhorros (self):
        self.__cuentaahorros.ConsignarValor(self.__cuentaahorros.DarSaldo())