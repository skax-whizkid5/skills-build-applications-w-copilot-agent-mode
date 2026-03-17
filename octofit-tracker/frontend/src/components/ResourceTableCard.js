import { useMemo, useState } from 'react';

function ResourceTableCard({ title, endpoint, rows, columns, loading, error, onRefresh }) {
  const [query, setQuery] = useState('');
  const [selectedRow, setSelectedRow] = useState(null);

  const filteredRows = useMemo(() => {
    const keyword = query.trim().toLowerCase();
    if (!keyword) {
      return rows;
    }

    return rows.filter((row) => {
      const values = Object.values(row || {});
      return values.some((value) => String(value ?? '').toLowerCase().includes(keyword));
    });
  }, [query, rows]);

  const closeModal = () => setSelectedRow(null);

  return (
    <>
      <section className="card shadow-sm border-0">
        <div className="card-header bg-white d-flex flex-column flex-md-row align-items-md-center justify-content-between gap-2">
          <div>
            <h2 className="h5 mb-1">{title}</h2>
            <a
              className="link-primary link-offset-2 link-underline-opacity-25 link-underline-opacity-100-hover"
              href={endpoint}
              target="_blank"
              rel="noreferrer"
            >
              REST API endpoint
            </a>
          </div>
          <button type="button" className="btn btn-primary btn-sm" onClick={onRefresh}>
            Refresh
          </button>
        </div>

        <div className="card-body">
          <form className="row g-2 align-items-end mb-3" onSubmit={(event) => event.preventDefault()}>
            <div className="col-md-7 col-lg-6">
              <label htmlFor={`${title}-search`} className="form-label small fw-semibold mb-1">
                Search rows
              </label>
              <input
                id={`${title}-search`}
                type="text"
                className="form-control"
                value={query}
                onChange={(event) => setQuery(event.target.value)}
                placeholder="Type to filter table data"
              />
            </div>
            <div className="col-auto">
              <button
                type="button"
                className="btn btn-outline-secondary"
                onClick={() => setQuery('')}
              >
                Clear
              </button>
            </div>
          </form>

          {loading ? <div className="empty-state">로딩 중...</div> : null}
          {error ? <div className="alert alert-danger mb-3">{error}</div> : null}

          {!loading && !error ? (
            <div className="table-responsive">
              <table className="table table-bordered table-hover table-striped align-middle table-sm mb-0 consistent-table">
                <thead className="table-light">
                  <tr>
                    {columns.map((column) => (
                      <th key={column.key} scope="col" className={column.headerClassName || ''}>
                        {column.label}
                      </th>
                    ))}
                    <th scope="col" className="text-center">Actions</th>
                  </tr>
                </thead>
                <tbody>
                  {filteredRows.length === 0 ? (
                    <tr>
                      <td colSpan={columns.length + 1} className="text-center text-secondary py-4">
                        데이터가 없습니다.
                      </td>
                    </tr>
                  ) : (
                    filteredRows.map((row, index) => (
                      <tr key={row.object_id || row.id || `${title}-${index}`}>
                        {columns.map((column) => (
                          <td key={`${column.key}-${row.object_id || row.id || index}`} className={column.cellClassName || ''}>
                            {column.render ? column.render(row[column.key], row) : String(row[column.key] ?? '-')}
                          </td>
                        ))}
                        <td className="text-center">
                          <button
                            type="button"
                            className="btn btn-outline-dark btn-sm"
                            onClick={() => setSelectedRow(row)}
                          >
                            Details
                          </button>
                        </td>
                      </tr>
                    ))
                  )}
                </tbody>
              </table>
            </div>
          ) : null}
        </div>
      </section>

      {selectedRow ? (
        <>
          <div className="modal fade show d-block" tabIndex="-1" role="dialog" aria-modal="true">
            <div className="modal-dialog modal-lg modal-dialog-scrollable">
              <div className="modal-content">
                <div className="modal-header">
                  <h5 className="modal-title">{title} details</h5>
                  <button type="button" className="btn-close" aria-label="Close" onClick={closeModal} />
                </div>
                <div className="modal-body">
                  <pre className="mb-0"><code>{JSON.stringify(selectedRow, null, 2)}</code></pre>
                </div>
                <div className="modal-footer">
                  <button type="button" className="btn btn-secondary" onClick={closeModal}>
                    Close
                  </button>
                </div>
              </div>
            </div>
          </div>
          <div className="modal-backdrop fade show" onClick={closeModal} />
        </>
      ) : null}
    </>
  );
}

export default ResourceTableCard;
