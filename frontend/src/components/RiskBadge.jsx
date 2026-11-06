import React from 'react';
export default function RiskBadge({category}){return <span className={'risk-badge '+String(category||'').toLowerCase().replace(' ','-')}>{category||'—'}</span>}
