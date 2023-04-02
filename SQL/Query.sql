SELECT
  em.nome,
  'Documento ' || cr.documento as DOCUMENTO,
  CAST(cr.valor AS NUMERIC(10,2)) as A_PAGAR,
  CAST(bx.valor AS NUMERIC(10,2)) as PAGO,
  SUBSTRING(CAST(cr.emissao as DATE) FROM 9 FOR 2) || '/' ||
  SUBSTRING(CAST(cr.emissao as DATE) FROM 6 FOR 2) || '/' ||
  SUBSTRING(CAST(cr.emissao as DATE) FROM 1 FOR 4) as DATA_LANCAMENTO,

  SUBSTRING(CAST(cr.vencto as DATE) FROM 9 FOR 2) || '/' ||
  SUBSTRING(CAST(cr.vencto as DATE) FROM 6 FOR 2) || '/' ||
  SUBSTRING(CAST(cr.vencto as DATE) FROM 1 FOR 4) as VENCIMENTO,

  SUBSTRING(CAST(bx.transmissao as DATE) FROM 9 FOR 2) || '/' ||
  SUBSTRING(CAST(bx.transmissao as DATE) FROM 6 FOR 2) || '/' ||
  SUBSTRING(CAST(bx.transmissao as DATE) FROM 1 FOR 4) as CONFIRMA_PAGAMENTO,

  SUBSTRING(CAST(bx.baixa as DATE) FROM 9 FOR 2) || '/' ||
  SUBSTRING(CAST(bx.baixa as DATE) FROM 6 FOR 2) || '/' ||
  SUBSTRING(CAST(bx.baixa as DATE) FROM 1 FOR 4) as DT_RECEBIDO
FROM CRD111 as cr
LEFT JOIN BXD111 as bx ON cr.documento = bx.documento
JOIN EMD101 as em ON cr.CGC_CPF = em.cgc_cpf
UNION
SELECT
  em.nome,
  ma.nome_tipo,
  ma.valor_orig,
  ma.valor,
  SUBSTRING(CAST(ma.emissao as DATE) FROM 9 FOR 2) || '/' ||
  SUBSTRING(CAST(ma.emissao as DATE) FROM 6 FOR 2) || '/' ||
  SUBSTRING(CAST(ma.emissao as DATE) FROM 1 FOR 4) as emissao,

  SUBSTRING(CAST(ma.vencto as DATE) FROM 9 FOR 2) || '/' ||
  SUBSTRING(CAST(ma.vencto as DATE) FROM 6 FOR 2) || '/' ||
  SUBSTRING(CAST(ma.vencto as DATE) FROM 1 FOR 4) as vencto,

  SUBSTRING(CAST(ma.data_pagto as DATE) FROM 9 FOR 2) || '/' ||
  SUBSTRING(CAST(ma.data_pagto as DATE) FROM 6 FOR 2) || '/' ||
  SUBSTRING(CAST(ma.data_pagto as DATE) FROM 1 FOR 4) as data_pagto,


  SUBSTRING(CAST(ma.data_modificado as DATE) FROM 9 FOR 2) || '/' ||
  SUBSTRING(CAST(ma.data_modificado as DATE) FROM 6 FOR 2) || '/' ||
  SUBSTRING(CAST(ma.data_modificado as DATE) FROM 1 FOR 4) as vencto
FROM MAN111 as ma
JOIN EMD101 as em ON ma.CNPJ_CPF = em.cgc_cpf