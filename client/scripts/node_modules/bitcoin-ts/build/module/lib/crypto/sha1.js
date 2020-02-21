import { instantiateRustWasm, sha1Base64Bytes } from '../bin/bin';
import { base64ToBin } from '../utils/utils';
/**
 * The most performant way to instantiate sha1 functionality. To avoid
 * using Node.js or DOM-specific APIs, you can use `instantiateSha1`.
 *
 * @param webassemblyBytes A buffer containing the sha1 binary.
 */
export const instantiateSha1Bytes = async (webassemblyBytes) => {
    const wasm = await instantiateRustWasm(webassemblyBytes, './sha1', 'sha1', 'sha1_init', 'sha1_update', 'sha1_final');
    return {
        final: wasm.final,
        hash: wasm.hash,
        init: wasm.init,
        update: wasm.update
    };
};
export const getEmbeddedSha1Binary = () => base64ToBin(sha1Base64Bytes).buffer;
/**
 * An ultimately-portable (but slower) version of `instantiateSha1Bytes`
 * which does not require the consumer to provide the sha1 binary buffer.
 */
export const instantiateSha1 = async () => instantiateSha1Bytes(getEmbeddedSha1Binary());
//# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoic2hhMS5qcyIsInNvdXJjZVJvb3QiOiIiLCJzb3VyY2VzIjpbIi4uLy4uLy4uLy4uL3NyYy9saWIvY3J5cHRvL3NoYTEudHMiXSwibmFtZXMiOltdLCJtYXBwaW5ncyI6IkFBQUEsT0FBTyxFQUFnQixtQkFBbUIsRUFBRSxlQUFlLEVBQUUsTUFBTSxZQUFZLENBQUM7QUFDaEYsT0FBTyxFQUFFLFdBQVcsRUFBRSxNQUFNLGdCQUFnQixDQUFDO0FBcUQ3Qzs7Ozs7R0FLRztBQUNILE1BQU0sQ0FBQyxNQUFNLG9CQUFvQixHQUFHLEtBQUssRUFDdkMsZ0JBQTZCLEVBQ2QsRUFBRTtJQUNqQixNQUFNLElBQUksR0FBRyxNQUFNLG1CQUFtQixDQUNwQyxnQkFBZ0IsRUFDaEIsUUFBUSxFQUNSLE1BQU0sRUFDTixXQUFXLEVBQ1gsYUFBYSxFQUNiLFlBQVksQ0FDYixDQUFDO0lBQ0YsT0FBTztRQUNMLEtBQUssRUFBRSxJQUFJLENBQUMsS0FBSztRQUNqQixJQUFJLEVBQUUsSUFBSSxDQUFDLElBQUk7UUFDZixJQUFJLEVBQUUsSUFBSSxDQUFDLElBQUk7UUFDZixNQUFNLEVBQUUsSUFBSSxDQUFDLE1BQU07S0FDcEIsQ0FBQztBQUNKLENBQUMsQ0FBQztBQUVGLE1BQU0sQ0FBQyxNQUFNLHFCQUFxQixHQUFHLEdBQWdCLEVBQUUsQ0FDckQsV0FBVyxDQUFDLGVBQWUsQ0FBQyxDQUFDLE1BQU0sQ0FBQztBQUV0Qzs7O0dBR0c7QUFDSCxNQUFNLENBQUMsTUFBTSxlQUFlLEdBQUcsS0FBSyxJQUFtQixFQUFFLENBQ3ZELG9CQUFvQixDQUFDLHFCQUFxQixFQUFFLENBQUMsQ0FBQyJ9