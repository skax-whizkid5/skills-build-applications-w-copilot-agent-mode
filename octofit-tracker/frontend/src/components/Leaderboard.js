import { useEffect, useState } from 'react';
import ResourceTableCard from './ResourceTableCard';
import { normalizeApiList } from '../utils/normalizeApiList';

function Leaderboard({ apiBaseUrl }) {
  const [entries, setEntries] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const [reloadToken, setReloadToken] = useState(0);
  const leaderboardApiUrl = `${apiBaseUrl.replace(/\/$/, '')}/api/leaderboard/`;

  useEffect(() => {
    const controller = new AbortController();

    const fetchLeaderboard = async () => {
      try {
        setLoading(true);
        setError('');

        const response = await fetch(leaderboardApiUrl, {
          signal: controller.signal,
        });

        if (!response.ok) {
          throw new Error(`HTTP ${response.status}`);
        }

        const data = await response.json();
        const items = normalizeApiList(data);
        console.log('[Leaderboard] endpoint:', leaderboardApiUrl);
        console.log('[Leaderboard] API payload:', data);
        console.log('[Leaderboard] normalized items:', items);
        setEntries(items);
      } catch (err) {
        if (err.name !== 'AbortError') {
          setError(`리더보드 데이터를 불러오지 못했습니다. (${err.message})`);
        }
      } finally {
        setLoading(false);
      }
    };

    fetchLeaderboard();

    return () => controller.abort();
  }, [leaderboardApiUrl, reloadToken]);

  const columns = [
    { key: 'rank', label: 'rank' },
    { key: 'user', label: 'user', cellClassName: 'mono-id' },
    { key: 'score', label: 'score' },
    {
      key: 'object_id',
      label: 'object_id',
      cellClassName: 'mono-id',
      render: (value, row) => value || row.id || '-',
    },
  ];

  return (
    <ResourceTableCard
      title="Leaderboard"
      endpoint={leaderboardApiUrl}
      rows={entries}
      columns={columns}
      loading={loading}
      error={error}
      onRefresh={() => setReloadToken((current) => current + 1)}
    />
  );
}

export default Leaderboard;
